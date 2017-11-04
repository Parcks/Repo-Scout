![Repo scout](RepoScout.png)
# Repo-Scout
Searches for a file in a VCS

## Usage
### Within a script
```python
>>> from service.repo_scout import RepoScout
>>> scout = RepoScout('GitHub')
>>> scout.find('Parcks','plugins','Laravel.ppl')
u'https://raw.githubusercontent.com/Parcks/plugins/master/debian/Laravel.ppl'
```

### From the CLI
```sh
jvalck@Setarit-DTP:~/repo_scout$ python main.py GitHub Parcks plugins Laravel.ppl
https://raw.githubusercontent.com/Parcks/plugins/master/debian/Laravel.ppl
```
