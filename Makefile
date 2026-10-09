SPEC = smartmet-swagger-ui

# Only the spec is stored in this repository. The source tarball is downloaded
# next to it from the URL in the spec.

RPMBUILD = rpmbuild --define "_sourcedir $(CURDIR)"

.PHONY: all sources srpm rpm unpack clean

all:
	@echo "Use 'make rpm' to download the sources and build the RPM package."

sources:
	spectool -g -C $(CURDIR) $(SPEC).spec

srpm: sources
	$(RPMBUILD) -bs $(SPEC).spec

rpm: sources
	$(RPMBUILD) -ba $(SPEC).spec

# Unpack the installed file set into ./dist for running plugin tests without
# installing the RPM (point the plugin's openapi.swagger_ui_dir at it).
unpack: sources
	rm -rf dist package
	tar -xzf swagger-ui-dist-*.tgz
	mkdir -p dist
	cp package/swagger-ui-bundle.js package/swagger-ui-standalone-preset.js \
	   package/swagger-ui.css package/favicon-16x16.png package/favicon-32x32.png dist/
	rm -rf package

clean:
	rm -rf *.tgz dist package
