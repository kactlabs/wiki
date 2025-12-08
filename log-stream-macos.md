/ [Home](index.md)

## Log Stream (Journalctl equivalent in MacOS)

**Note:** 

Below are **macOS `log` command equivalents** for the `journalctl` examples you provided.

---

### 1. `journalctl --since "2022-02-01"`

macOS equivalent:

```bash
log show --start "2022-02-01"
```

---

### 2. `journalctl --since "2022-02-01 00:24:41" --until "2022-02-02"`

macOS equivalent:

```bash
log show --start "2022-02-01 00:24:41" --end "2022-02-02"
```

---

### 3. With output redirected to a log file

#### journalctl:

```bash
journalctl --since "2022-02-01 00:24:41" --until "2022-02-02" >> minio_error.log
```

#### Mac:

```bash
log show --start "2022-02-01 00:24:41" --end "2022-02-02" >> minio_error.log
```

---

### (Optional) Filtering `log show` to specific process/service (closest to `-u servicename`)

Example for filtering for MinIO:

```bash
log show --start "2022-02-01" --end "2022-02-02" \
  --predicate 'process == "minio"' >> minio_error.log
```

Generic predicate examples:

* contains text:

  ```bash
  --predicate 'eventMessage CONTAINS "error"'
  ```
* matches process & contains keyword:

  ```bash
  --predicate 'process == "minio" AND eventMessage CONTAINS "timeout"'
  ```

---

### If you want live streaming (equivalent of `journalctl -f`)

Tail live logs:

```bash
log stream
```

Tail live logs with process filter:

```bash
log stream --predicate 'process == "minio"'
```

---
