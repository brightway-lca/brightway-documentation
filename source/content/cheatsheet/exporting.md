# Exporting Data or Projects

## Basic Operations

### How do I share share my entire project with someone else?

```python
bi.backup.backup_project_directory(project="<my_project>", dir_backup="<target_directory>")
```

You can restore the project with:

```python
bi.backup.restore_project_directory(fp="<backup_file.tar.gz>")
```