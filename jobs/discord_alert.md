# Discord Alert for automatic Jobs

MAD will be able to submit job stats to Discord.

## setup config.ini for Discord submission

```
# Job Status Messages
######################
#job_dt_wh                    # Send job status to discord (Default: False)
#job_dt_wh_url:               # Discord Webhook URL for job messages
#job_dt_send_type:            # Kind of Job Messages to send - separated by pipe | (Default: SUCCESS|FAILURE|NOCONNECT|TERMINATED)
```

- `job_dt_wh`: Enable Discord submission
- `job_dt_wh_url`: Discord Bot Webhook URL
- `job_dt_send_type`: Define the kind of submission (separated by pipe | ) (Default: SUCCESS|FAILURE|NOCONNECT|TERMINATED)

## Examples

![](../_static/jobs/Jobs_DT_job1.png)
![](../_static/jobs/Jobs_DT_job2.png)
![](../_static/jobs/Jobs_DT_job3.png)