sam validate -t template.yaml
sam build
sam package --output-template-file packaged.yaml --s3-bucket svz-sam
sam deploy --template-file packaged.yaml --stack-name cloudtrail-log-analytics --capabilities CAPABILITY_IAM --parameter-overrides ESDomain=$ES_DOMAIN ESFullDomain=$ES_PATH

