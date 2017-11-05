![Repo scout](RepoScout.png)
# Repo-Scout
Searches for a file in a VCS

---

## Usage
### Within a script
```python
>>> from service.repo_scout import RepoScout
>>> scout = RepoScout('GitHub')
>>> scout.find('Parcks','plugins','Laravel.ppl')
u'https://raw.githubusercontent.com/Parcks/plugins/master/debian/Laravel.ppl'
```

### From the CLI
#### Parameters
```sh
  -h, --help           show this help message and exit
  -p, --provider PROV  The name of the VCS provider (Default: GitHub)
  -o, --owner OWNER    The name of the owner of the repository
  -n, --name NAME      The name of the repository to search in
  -m, --method METHOD  Indicates if the file should be searched in a directory
                       or just retrieve the first occurrence (Default: First)
  -f, --file FILE      The name of the file to find
  -d, --directory DIR  The path in the repository where the file should be
                       searched
```
#### Example
##### Find first occurrence
```sh
jvalck@Setarit-DTP:~/repo_scout$ python main.py -o Parcks -n plugins -f Laravel.ppl
https://raw.githubusercontent.com/Parcks/plugins/master/debian/Laravel.ppl
```
##### Find in directory
- Example 1: One level deep
```sh
jvalck@Setarit-DTP:~/repo_scout$ rscout -o Parcks -n plugins -f Laravel.ppl -m InDirectory -d debian
https://raw.githubusercontent.com/Parcks/plugins/master/debian/Laravel.ppl
```
- Example 2: two levels deep
```sh
jvalck@Setarit-DTP:~/repo_scout$ rscout -o Parcks -n core -f user_input.py -m InDirectory -d src/cli
https://raw.githubusercontent.com/Parcks/core/master/src/cli/user_input.py
```
