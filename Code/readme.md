# Churn Classification

Run CATelcoCustomerChurnModeling.py in local environment.
```
$ az ml experiment submit -c local CATelcoCustomerChurnModeling.py
```

Run iris_sklearn.py in a local Docker container.
```
$ az ml experiment submit -c docker CATelcoCustomerChurnModelingDocker.py
