# Rat API

## Overview

This Rat API gives you access to multiple Rat Pictures and Rat Facts. Rat Pictures are returned in .JPG format. Rat Facts are returned as JSON. 

## URL

Currently, this API is not hosted and needs to be run locally. 

To get started download the files above and run app.py by typing `python app.py` in the terminal. 

The URL will be http://127.0.0.1:5000/. This will bring you to the home page which explains how to use the API. 

## Authentication

No Authentication needed. 

## Endpoints

### 1. Image Amount

- Endpoint: `/get-pic-amount`
- Method: GET
- Response: Total amount of images currently available e.g. `05`.

### 2. Rat Images

- Endpoint: `/get-rat/<rat-id>`
- Method: GET
- Parameters: `rat-id` (required). The number rat you want, max value is Image Amount.
- Example Request:

    ```
    /get-rat/05
    ```
- Response: .jpg file.

### 3. Rat Facts

- Endpoint: `/get-rat-facts`
- Method: GET
- Response: Rat facts in JSON format. 

## Error Handling

The API returns the appropriate HTTP status code.




