from datetime import datetime

timestamp = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
prowler_version = "3.0-alfa"

# Groups
groups_file = "groups.json"

# AWS services-regions matrix json
aws_services_json_url = (
    "https://api.regional-table.region-services.aws.a2z.com/index.json"
)
aws_services_json_file = "providers/aws/aws_regions_services.json"