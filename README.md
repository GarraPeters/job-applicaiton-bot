# jobserve-apply-robot

Automatic job applications.

### Installation

First checkout this repository and `cd` into it.

```
pip install -r requirements.txt
```

### Usage

1. First install chromedriver on your machine, selenium needs this to work.

2. Fill out your account profile, you **must** upload your CV at this point otherwise it will not work.

Now you just need your login email, password and job search url.

To get the job search url to go https://www.jobserve.com/gb/en/Candidate/Home.aspx

Search for the job you'd like and copy the url of the result page.

For example https://www.jobserve.com/gb/en/JobSearch.aspx?shid=EEB9AF7ED1752E4FC6.

3. Run the program:

```
python apply.py --email="john@example.com" --password="xxxxx"
--search-url="https://www.jobserve.com/gb/en/JobSearch.aspx?shid=EEB9AF7ED1752E4FC6"
```


The program will run and apply to all jobs continously. It will use the CV from your profile for applications.

Example terminal output:

```
ALREADY_APPLIED: Java Kotlin Technical Architect (hands on with code), Central London, eCommerce, excellent rates
ALREADY_APPLIED: Java Developer - Low Latency Multi-threaded Credit eTrading - Investment Bank
APPLIED TO: Java Developer - FX - Canary Wharf - £700-£800
APPLIED TO: Java Developer
```
