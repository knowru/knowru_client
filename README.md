knowru_client
=============
Client to run runnables inside Knowru

Usage
-----
* Basic usage
```
kc = KnowruClient("your-token", "your-knowru-url")
kc.run_runnable("runnable-name", {"input": "data"})
```

* Advanced usage
    * Due to network unstability, requests can inermittently fail. In the above case, such failures will result in `requests.exceptions.RetryError`. To avoid it, provide an output value to return when an exception happens.
```
kc = KnowruClient("your-token", "your-knowru-url")
kc.run_runnable("runnable-name", {"input": "data"}, {"default": "output"})
```

Installation
--------------
```
pip install knowru_client
```


Contact
-------
* Knowru, LLC (hello@knowru.com / [https://www.knowru.com](https://www.knowru.com))