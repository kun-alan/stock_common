# stock_common

This repository contains reusable code, such as utilities (convenience functions and classes), which will be used by the `stock_recommender`, `stock_watcher` and `stock_advisor` repositories.


## Create/Update virutal environment from environment.yml
https://conda.io/docs/user-guide/tasks/manage-environments.html

export env to yml
```
source activate kun_alan
conda env export > environment.yml
```

create env from yml
```
conda env create -f environment.yml
```

update env from yml
```
conda env update -f environment.yml
```


