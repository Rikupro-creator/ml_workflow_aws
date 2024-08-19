This is an end to end ML project in AWS. It makes use of AWS sagemaker, lambdas, and stepfunction to create a complete project. 

The first file in this directory is the started notebook which is created from sagemaker. In it alot of process which involved data collection, data cleaning and fitting an inbuilt sagemaker model for image classification. After creating an endpoint, we create three lambda functions . The first one serializes the image, the second one makes inferences and the third one thresholds the predictions to ones which the model is 70% sure. 

Finally, step functions are created and the execution-detail.json file provided a json format of how the step execuation was performed. 

Point to note, in all the lambdas, permissions are given for S3 full access policy, lambda execution, and sagemaker full access policy. 