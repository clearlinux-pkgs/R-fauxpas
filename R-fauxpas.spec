#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fauxpas
Version  : 0.5.0
Release  : 22
URL      : https://cran.r-project.org/src/contrib/fauxpas_0.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fauxpas_0.5.0.tar.gz
Summary  : HTTP Error Helpers
Group    : Development/Tools
License  : MIT
Requires: R-R6
Requires: R-crul
Requires: R-httpcode
Requires: R-whisker
BuildRequires : R-R6
BuildRequires : R-crul
BuildRequires : R-httpcode
BuildRequires : R-whisker
BuildRequires : buildreq-R

%description
error handling, as well as individual methods for every HTTP status
    code, both via status code numbers as well as their descriptive names.
    Supports ability to adjust behavior to stop, message or warning.
    Includes ability to use custom whisker template to have any configuration
    of status code, short description, and verbose message. Currently 
    supports integration with 'crul', 'curl', and 'httr'.

%prep
%setup -q -c -n fauxpas
cd %{_builddir}/fauxpas

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589772220

%install
export SOURCE_DATE_EPOCH=1589772220
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fauxpas
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fauxpas
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fauxpas
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fauxpas || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fauxpas/DESCRIPTION
/usr/lib64/R/library/fauxpas/INDEX
/usr/lib64/R/library/fauxpas/LICENSE
/usr/lib64/R/library/fauxpas/Meta/Rd.rds
/usr/lib64/R/library/fauxpas/Meta/features.rds
/usr/lib64/R/library/fauxpas/Meta/hsearch.rds
/usr/lib64/R/library/fauxpas/Meta/links.rds
/usr/lib64/R/library/fauxpas/Meta/nsInfo.rds
/usr/lib64/R/library/fauxpas/Meta/package.rds
/usr/lib64/R/library/fauxpas/Meta/vignette.rds
/usr/lib64/R/library/fauxpas/NAMESPACE
/usr/lib64/R/library/fauxpas/NEWS.md
/usr/lib64/R/library/fauxpas/R/fauxpas
/usr/lib64/R/library/fauxpas/R/fauxpas.rdb
/usr/lib64/R/library/fauxpas/R/fauxpas.rdx
/usr/lib64/R/library/fauxpas/doc/fauxpas-vignette.R
/usr/lib64/R/library/fauxpas/doc/fauxpas-vignette.Rmd
/usr/lib64/R/library/fauxpas/doc/fauxpas-vignette.html
/usr/lib64/R/library/fauxpas/doc/index.html
/usr/lib64/R/library/fauxpas/help/AnIndex
/usr/lib64/R/library/fauxpas/help/aliases.rds
/usr/lib64/R/library/fauxpas/help/fauxpas.rdb
/usr/lib64/R/library/fauxpas/help/fauxpas.rdx
/usr/lib64/R/library/fauxpas/help/paths.rds
/usr/lib64/R/library/fauxpas/html/00Index.html
/usr/lib64/R/library/fauxpas/html/R.css
/usr/lib64/R/library/fauxpas/tests/test-all.R
/usr/lib64/R/library/fauxpas/tests/testthat/cached_teapot.rda
/usr/lib64/R/library/fauxpas/tests/testthat/test-Error.R
/usr/lib64/R/library/fauxpas/tests/testthat/test-children.R
/usr/lib64/R/library/fauxpas/tests/testthat/test-fail-well.R
/usr/lib64/R/library/fauxpas/tests/testthat/test-http.R
/usr/lib64/R/library/fauxpas/tests/testthat/test-http_star.R
