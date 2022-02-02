import argparse
import requests

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--breed', action='store', type=str, required=True)
my_parser.add_argument('--list', action='store_true')
my_parser.add_argument('--count', action='store_true')
my_parser.add_argument('--image', action='store_true')

args = my_parser.parse_args()

## Define the URLs to GET Request
url = f"https://dog.ceo/api/breed/{args.breed}/list"
url_image = f"https://dog.ceo/api/breed/{args.breed}/images/random"

## Get Request and Data Structure (Dictionary)
resp = requests.get(url=url)
data = resp.json()

## Get Request and Data Structure (Dictionary) for the Image
resp_image = requests.get(url=url_image)
data_image = resp_image.json()

## Show the Result
if data['status'] == 'error':
    print(f"Breed {args.breed} NOT FOUND")
else:
   print(f"Breed {args.breed} FOUND")
   if args.list:
       print(f"The {args.breed} sub-breed are : {data['message']}")
   if args.count:
       print(f"There are {len(data['message'])} {args.breed} sub-breed")
   if args.image:
       print(f"See the Image : {data_image['message']}")
