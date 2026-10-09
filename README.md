# smartmet-swagger-ui

RPM repackaging of the [Swagger UI](https://github.com/swagger-api/swagger-ui)
browser bundle (`swagger-ui-dist` npm package) for SmartMet Server.

The edr, wms and download plugins serve a human-readable description of their
APIs at `<api root>/api/docs`. That page is rendered by Swagger UI from the
OpenAPI definition the plugin generates. The JavaScript and CSS files are
installed to `/usr/share/smartmet/swagger-ui` and served by the plugins
themselves, so the documentation pages work without access to any public CDN.

    make rpm      # download the source tarball and build the RPM
    make unpack   # extract the installed file set into ./dist for local tests
