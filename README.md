# tg_admin
Bot that will admin your telegram channel and shitpost like a god

### How to run
1. Go to the project's folder
```
cd tg_admin/
```

2. In the directory `tg_admin` create file `config.py` based on `config_template.py` which you can find in the same directory.

2. Set up the database (`Docker` needed)
```
make db
```

3. Install the dependencies (`Poetry` needed)
```
make install 
```

4. Enter the poetry shell
```
make shell
```

5. Run
```
make run
```
