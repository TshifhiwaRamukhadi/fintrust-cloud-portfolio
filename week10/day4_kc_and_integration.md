# Week 10 Day 4: Python Knowledge Check, SQL Knowledge Check and Integration Challenge

## Objective

Review and consolidate the concepts covered during Week 10, including Python package development, migration automation with boto3, SQL Views, DataSync automation, DMS monitoring, and migration reporting.

---

# Python Knowledge Check

## Q1: What determines which names are imported when using `from fintrust_migration import *`?

If `__all__` is defined in `__init__.py`, only the names listed in the `__all__` variable are imported. If `__all__` is not defined, Python imports all names that do not begin with an underscore (`_`).

The main risk of not defining `__all__` is that internal helper functions and variables may become publicly accessible unintentionally. This can lead to namespace pollution, accidental misuse of internal code, and increased maintenance complexity.

---

## Q2: What pattern is used by the boto3 session factory and why is it important?

The boto3 session factory uses the Singleton pattern.

A module-level variable stores a single session object:

```python
_session = None
```

The session is created only once:

```python
if _session is None:
    _session = boto3.Session()
```

Benefits include:

- Reduced initialization overhead
- Faster execution of multiple AWS API calls
- Consistent configuration across the application
- Reuse of credential and connection settings
- Improved maintainability

This is especially useful when performing dozens of boto3 operations during migration activities.

---

## Q3: What happens if `start-replication` is used during a CDC migration phase?

Using:

```python
StartReplicationTaskType='start-replication'
```

causes AWS DMS to restart the migration from the beginning and reload target tables.

This can result in:

- Deletion of existing migrated data
- Loss of CDC progress
- Increased migration downtime

To resume an existing replication task safely, the following should be used:

```python
StartReplicationTaskType='resume-processing'
```

This continues from the last checkpoint rather than restarting the migration.

---

## Q4: Which AWS service schedules DataSync bandwidth changes?

Amazon EventBridge Scheduler is used to schedule automated DataSync bandwidth adjustments.

FinTrust requires:

- 500 Mbps during business hours
- 9 Gbps overnight

Because SAST is UTC+2:

```text
22:00 SAST = 20:00 UTC
```

The EventBridge Scheduler cron expression is:

```text
cron(0 20 * * ? *)
```

---

## Q5: Why can a DataS*nc task display RUNNING while show*ng zero bytes transferred?

DataSy*c performs a preparation phase bef*re transferring files.

During thi* phase DataSync:

- Enumerates sou*ce files
- Validates source locati*ns
- Builds transfer manifests
- P*epares transfer metadata*
As a result:

```text
Status = RU*NING
BytesTransferred =*0
```

is expected behavior*until actual file transfer begins.*
---

# SQL Knowledge Check

*# Q1: How do Views protect dashboa*ds from schema changes?

*iews act as a stable interface bet*een applications and database tabl*s.

For example, suppose a dashboa*d queries:

```sql
v_monthly*txn_summary
```

and the underlyin* column:

```sql
customers.segment*```

is renamed to:

*``sql
customers.customer_segment
`*`

The dashboard remains unaffecte* because only the view definition *eeds updating:

```sql
SELECT
    *ustomer_segment AS segment
```

*pplications*continue querying the same view*without modification.

---

*# Q2: Create a view showing*migration wave completion percenta*e

```sql
CREATE OR REPLACE VIEW v*wave_pct AS
SELECT
    migration_w*ve,
    COUNT(*) AS total,
    SUM*
        CASE
            WHEN sta*us = 'C'
            THEN 1
      *     ELSE 0
        END
    ) AS c*mplete,
    ROUND*
        100*0 *
        SUM(
            CASE
*               WHEN status = 'C'
 *              THEN 1
             *  ELSE 0
            END
        )*/ COUNT(*),
        1
    ) AS pct*complete
FROM migration_plan
GROUP*BY migration_wave;
```

This view *rovides:

- Migration wave number
* Total assets
- Completed assets
-*Percentage completion

---

## Q3:*What is the difference between a V*ew and a Materialized View?

### S*andard View

A View stores only*the query definition.

Every time *t is queried:

```sql*SELECT * FROM my_view;
```

*he underlying query executes again*

Benefits:

* Always current
- No*storage*requirements
- Easy to maintain

L*mitations*

- Potentially slower on large da*asets

---

### Materialized View
*A Materialized View stores the que*y results physically.

Example ref*esh:

```sql
REF*ESH MATERIALIZED VIEW my_materiali*ed_view;
```

Benefits:

- Faster *eporting
- Reduced query load
- Su*table*for*BI dashboards

Limitations:

* Data may become stale between ref*eshes

Materialized Views are usef*l when aggregation queries process*millions or billions of rows.

---*
## Q4: What does NULLIF do?

`NUL*IF(expression, value)` returns:

`*`sql
NULL
```

when:

```sql
expre*sion = value
```

Otherwise*it returns the expression.

Exampl*:

```sql
NULLIF(total_size_gb, 0)*```

prevents division by zero.

W*thout NULLIF:

```sql
100 / 0
*``

causes an error.

With NULLIF:*
*``sql
100 / NULL
```

returns:

``*sql
NULL
```

*his prevents dashboard failures an* allows reporting tools to display*blank values safely.

---

# Integ*ation Challenge

## FinTrust Migra*ion Orchestrator Workflow

The mig*ation orchestrator combines all mo*ules developed during Week 10 into*a single automated workflow.

### *tep 1: Classify EC2 Instances

The*EC2 classifier identifies instance* according to migration strategy:
*- Rehost
- Replatform
- Refactor
-*Repurchase
- Retain
- Retire

The *rchestrator selects:

```text*Wave 1 Rehost Instances*```

*--

### Step 2: Tag Instances

*elected instances receive the tag*

```text
migration:status = in-pr*gress
```

This indicates*that migration activity has starte*.

---

### Step 3: Start DMS

*he orchestrator starts the DMS Ful* Load and CDC task.

```text**ource Database
        ↓
AWS DMS
 *      ↓
Target Database
```

---

*## Step 4: Monitor CDC

The orches*rator continuously checks:

```tex*
CDCLatencySource
```

and evaluat*s cutover readiness.

The migratio* only proceeds when:

```text
*DCLatencySource < 30 seconds
```

*--

###*Step 5: Cutover Readiness Check

T*e orchestrator determines whether*

- Replication is healthy
- Lag i* acceptable*- Migration can safely proceed

--*

### Step 6: Run Final DataSync

* final DataSync execution is*started to synchronize remaining f*les.

```text
File Server*/ NAS
        ↓
AWS DataSync
     *  ↓
Amazon S3
``*

---

### Step 7* Wait for SUCCESS

The Data*ync execution is monitored until i* reaches:

```text
SUCCESS
```

*r

```*ext
ERROR
```

*--

### Step 8: Write Summary to A*azon S3

A JSON migration summary *s produced containing:

- Migratio* wave
- Cutover timestamp
- DMS st*tus
- DataSync*status
- Final migration result

-*-

## End-to-End Workflow Diagram
*```text
Class*fy EC2 Workloads
*           ↓
Identify Wave 1 Rehos* Systems
            ↓
Tag Resourc*s as In-Progress
            ↓
Sta*t DMS Migration*            ↓
Monitor CDC Lag
    *       ↓
Cutover*Ready?
            ↓
Run Final Dat*Sync
            ↓
Wait for SUCCES*
            ↓
Write JSON Summary *o S3
            ↓
Migration Compl*te
```

---

# Week*10 Reflection

## Automation ROI

*he FinTrust Migration*Package automates tasks that would*otherwise require significant manu*l effort from migration engineers.*
Automated capabilities include:

* EC2 migration classification
- Mi*ration wave tracking
- DMS task mo*itoring
- CDC lag monitoring
- Dat*Sync execution monitoring
- Dynami* bandwidth throttling
- Migration *eporting
- Transfer auditing

With*ut automation, engineers would spe*d time manually:

- Checking migra*ion status
- Monitoring replicatio* lag
- Monitoring transfer progres*
- Updating throttling settings
- *roducing reports
- Validating migr*tion readiness

Estimated savings:*
```text
3 hours per day
```

*``*ext
15 hours per week
```

*``text
210 hours during a 14-week *igration programme
```

Benefits i*clude:

- Faster migration executi*n
- Reduced operational overhead
-*Improved consistency
- Lower risk *f human error
- Better reporting a*d visibility
- More time for engin*ering and architecture activities
*The package demonstrates how reusa*le Python automation and SQL repor*ing can significantly improve effi*iency during large-scale cloud mig*ation programmes.

---

## Week 10*Summary

### Day 1

- fintrust_mig*ation package setup
- boto3 sessio* factory
- EC2 migration classific*tion
- SQL migration reporting*views

### Day 2

- DMS task manag*ment
- CDC lag monitoring
* CloudWatch integration
- Customer*and transaction reporting views

#*# Day 3

- DataSync task automatio*
- Dynamic bandwidth throttling
- *ventBridge scheduling
- BI reporti*g views

### Day 4

- Python Knowl*dge*Check
- SQL Knowledge Check
- Inte*ration Challenge
- Automation ROI *ssessment

Week 10*successfully demonstrated how Pyth*n automation and SQL reporting can be combined to support enterprise cloud migration programmes.
*