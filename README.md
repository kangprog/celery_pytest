# celery_pytest
파이썬 셀러리 동작을 Pytest로 Test 하기
<br></br>
---

### docker compose Command
```python
docker-compose -f docker-compose.yml up -d
```

### Celery Command
```python
Celery -A celery_app worker -l info -c 1
```

### pytest Command
```python
python -m pytest tests/test_celery_work.py
```