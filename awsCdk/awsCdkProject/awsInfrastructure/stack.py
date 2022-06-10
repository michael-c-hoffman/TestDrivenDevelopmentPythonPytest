import aws_cdk

from aws_cdk import (
    # Duration,
    Stack,
    aws_iam as iam,
    aws_s3 as s3,
    aws_lambda,
    aws_lambda_python_alpha as lambda_python,
)

from constructs import Construct


class AwsInfrastructureStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        bucket = s3.Bucket(
            self,
            "AwsInfrastructureBucket-1",
            versioned=True,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            removal_policy=aws_cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )
        bucket.grant_read_write(iam.AccountRootPrincipal())

        #  requestlambda = lambda_python.PythonFunction(
            #  self,
            #  "requestslambda",
            #  entry="awsInfrastructure/requestsLambda",
            #  runtime=aws_lambda.Runtime.PYTHON_3_9,
            #  index="requestslambda/lambdaModule.py",
            #  handler="handler",
            #  bundling=lambda_python.BundlingOptions(),
        #  )
