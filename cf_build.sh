sam validate -t template.yaml
sam build
sam package --output-template-file packaged.yaml --s3-bucket svz-sam