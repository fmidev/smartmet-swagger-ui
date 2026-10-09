#
# Swagger UI static files for the SmartMet Server OpenAPI documentation pages.
#
# The edr, wms and download plugins serve a human-readable API description at
# <api root>/api/docs. The page is rendered by Swagger UI from the OpenAPI
# definition the plugin generates. The JavaScript and CSS files are installed
# locally and served by the plugins themselves, so the documentation pages do
# not depend on any public CDN.
#
# The source is the upstream swagger-ui-dist npm package, which contains the
# prebuilt browser bundles. Only the files the documentation page needs are
# installed: the bundle, the standalone preset, the stylesheet, the favicons
# and the license files. Source maps and the ES module builds are left out.
#
# Sources are downloaded, not stored in the repository:
#
#   spectool -g -R smartmet-swagger-ui.spec    (or: make sources)
#   rpmbuild -ba smartmet-swagger-ui.spec      (or: make rpm)
#
# To update: change Version to a swagger-ui-dist release at least two weeks
# old, then rebuild.
#

%global upstream swagger-ui-dist

Name:           smartmet-swagger-ui
Version:        5.33.0
Release:        1%{?dist}.fmi
Summary:        Swagger UI static files for SmartMet Server API documentation
License:        Apache-2.0
URL:            https://github.com/swagger-api/swagger-ui
Source0:        https://registry.npmjs.org/%{upstream}/-/%{upstream}-%{version}.tgz
BuildArch:      noarch

%description
Swagger UI %{version} browser bundle, installed to %{_datadir}/smartmet/swagger-ui.
SmartMet Server plugins use it to render their generated OpenAPI definitions
as human-readable documentation at <api root>/api/docs.

%prep
%setup -q -n package

%build
# Nothing to build; the npm package contains the prebuilt browser bundles.

%install
mkdir -p %{buildroot}%{_datadir}/smartmet/swagger-ui
for f in swagger-ui-bundle.js swagger-ui-standalone-preset.js swagger-ui.css \
         favicon-16x16.png favicon-32x32.png; do
  install -m 0644 $f %{buildroot}%{_datadir}/smartmet/swagger-ui/$f
done

%files
%license LICENSE NOTICE swagger-ui-bundle.js.LICENSE.txt swagger-ui-standalone-preset.js.LICENSE.txt
%dir %{_datadir}/smartmet
%{_datadir}/smartmet/swagger-ui

%changelog
* Fri Oct  9 2026 Mika Heiskanen <mika.heiskanen@fmi.fi> - 5.33.0-1.fmi
- Initial package: swagger-ui-dist 5.33.0 for the SmartMet OpenAPI documentation pages
