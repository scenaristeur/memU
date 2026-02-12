```
pyenv install 3.13
memU$ python3.13 -m venv .venv
. .venv/bin/activate
curl https://sh.rustup.rs -sSf | sh
pip install e .
pip install python-dotenv
```

intégration d'Albert selon https://github.com/NevaMind-AI/memU/commit/cba667a56daca5093c9b79a598c7d2ffda813756

modèles et limites d'Albert : https://albert.sites.beta.gouv.fr/prices/

# issues

- 429

Processing conversations...
Processing: examples/resources/conversations/conv1_fr.json
Processing: examples/resources/conversations/conv2_fr.json
Error processing examples/resources/conversations/conv2_fr.json: Client error '429 Too Many Requests' for url 'https://albert.api.etalab.gouv.fr/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429
Processing: examples/resources/conversations/conv3_fr.json
Error processing examples/resources/conversations/conv3_fr.json: Client error '429 Too Many Requests' for url 'https://albert.api.etalab.gouv.fr/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429

limite 429 : https://stackoverflow.com/questions/22786068/how-to-avoid-http-error-429-too-many-requests-python
