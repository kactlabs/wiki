/ [Home](index.md)

# T-Scraper

**Note:** You need to have GitHub Access to Featurepreneur Organisation

 ---

1. Go to [T-Scraper](https://github.com/kactlabs/t-scraper)
2. Clone the repo
3. Install JDK by 
```
    sudo apt install openjdk-11-jdk
    sudo apt install openjdk-11-jre
```
4. Download browsermob-proxy zip file from: [http://bmp.lightbody.net/](http://bmp.lightbody.net/)
5. Extract the zip file
6. Open the `t-scraper` repo
7. Activate the Python Environment (miniconda)
8. Run ```pip install -r requirements.txt```
9. Duplicate the `.env.sample` file
10. Rename the duplicate file to `.env`
11. Replace the details in .env file, for basic setup use:
```
PROXY_PATH=<path-where-bmp-zip-was-extracted>/browsermob-proxy-2.1.4-bin/browsermob-proxy-2.1.4/bin/browsermob-proxy
DB_USERNAME=postgres
DB_PASSWORD=root
DB_HOST=localhost
DB_DATABASE=postgres
DB_PORT=5432
HAR_DUMP_TYPE=1
AWS_REGION=us-west-2
AWS_ACCESS_KEY_ID=test
AWS_SECRET_ACCESS_KEY_ID=test
ENDPOINT_URL=http://localhost:4566
BUCKET=t-scraper
```
12. Run the following commands
```
docker run --name pg11 -e POSTGRES_PASSWORD=root -d -p 5432:5432 postgres
docker exec -it pg11 bash
psql -h 0.0.0.0 -p 5432 -U postgres
```
13. Run all the Queries in `init.sql`
14. Exit out of the container (using ```exit``` command twice)
15. Run ```python app.py```
16. Open [http://192.168.1.150:5000/](http://192.168.1.150:5000/) in browser
17. Click Scrape Template on the Left Navigation Bar
18. Click Add More
19. Enter the Required Details and Click save  
For example:
```
Template Name = test-scanner-template
Retailer = Target
Scrape Type = Product
DriverExtras Override:
{
      "variables" : [
            "title",
            "price",
            "is_available_now",
            "highlights",
            "specifications",
            "description"
      ],
      "collect_reviews" : 1,
      "review_collect_action" : {
            "load_more_button_xpath" : "//div[@data-test='load-more-btn']/button",
            "load_more_click_count" : 5,
            "max_reviews" : 40
      },
      "postal_code" : 1, 
      "section_info" : [
            {
            "name" : "Details",
            "section_click_xpath" : ""
            },
            {
            "name" : "shipping_returns",
            "section_click_xpath" : ""
            },
            {
            "name" : "qa",
            "section_click_xpath" : ""
            }
      ],
      "collect_photos" : 1,
      "compress_photos" : 1,
      "photos_dump" : 1
}
Scrape Variables:
[
      "title",
      "price",
      "is_available_now",
      "highlights",
      "specifications",
      "description"
]
```
20.  Click Parse Template on the Left Navigation Bar
21. Click Add More
22. Enter the Required Details and Click save  
for example,
```
Template Name = test-parser-template
Retailer = Target
Scrape Type = Product
Scrape Variables:
      [
                {
                    "field": "title",
                    "type": "xpath",
                    "path": "//*[@data-test='product-title']/span/text()",
                    "endpoint": ""
                },
                {
                    "field": "price",
                    "type": "xpath",
                    "path": "//span[@class='h-text-red']/span/text()",
                    "endpoint": ""
                },
                {
                    "field": "highlights",
                    "type": "xpath",
                    "path": "//li[@class='styles__Bullet-sc-6aebpn-0 eIfLaI']/span/text()",
                    "endpoint": ""
                },
                {
                    "field": "specifications",
                    "type": "xpath",
                    "path": "//*[@data-test='item-details-specifications']/div/div/text()",
                    "endpoint": ""
                },
                {
                    "field": "description",
                    "type": "xpath",
                    "path": "//*[@data-test='item-details-description']/text()",
                    "endpoint": ""
                }
      ]
```
23. Go back to [http://192.168.1.150:5000/](http://192.168.1.150:5000/)
24. Click Batch Scan  on the Left Navigation Bar
25. Enter the name of the Scanner Template in Template Name and The links to be Scanned in URLs  
      (Incase of multiple links separate them by one link per line)
26. Click Save
27. Wait for the page to redirect to the Scanned URLs page
28.  Go back to [http://192.168.1.150:5000/](http://192.168.1.150:5000/)
29. Click Parse  on the Left Navigation bar
30. Enter the name of the Parser Template in Template Name and The link to be Scanned in URL
31. Click Save and Parsed output will be displayed below in JSON format

---

**Note:**  
To use LocalStack S3 in .env file set HAR_DUMP_TYPE=2 and the AWS credentials as given in above .env example and run ```docker-compose up ``` or ```docker-compose up -d``` from the root folder of the repo in another terminal

Or for AWS S3 set HAR_DUMP_TYPE=3 and the AWS credentials as Access keys of AWS account with S3 access in .env file

---
