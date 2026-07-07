#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print titles"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        r = r.json()
        for dictionary in r:
            print(dictionary['title'])


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save to CSV"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                    extrasaction='ignore')
            writer.writeheader()
            writer.writerows(r.json())
