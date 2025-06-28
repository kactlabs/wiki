/ [Home](index.md)

## POC Projects




#### Project 1
```
Capstone Projects / POC:
1. Image processing with AI assistance
	Dump the images into S3 bucket
	Listener will watch the images and if 10 product images dumped, it will trigger Lambda
	Lambda will call the MLAPI
	10 Product image bundle
		5 - 25 images in each product
			use AI to find the main image

	ML API will decide 
		Prodct 1 Images go to type<N>

		Will send AWS SQS 

	N workers (Celery worker instance)
		will check SQS 
			type = type1

		type1 
		..
		type4

		Processed images will be dumped into S3 Bucket (destination bucket)

	Flowers to check the worker progress

	Once the processing is done, we will send an email to the group
		Group 1
			raja@kactii.com
			vijitha@gmail.com

		Group 2
			..

	Worker Scaling will be based on SQS
		1 worker = 10 Products
		2 workers = 20 Proudcts

		5 workers = 50 Products

	ML will decide which worker to do the image process
```


