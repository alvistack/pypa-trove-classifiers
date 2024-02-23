# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-trove-classifiers
Epoch: 100
Version: 2024.4.10
Release: 1%{?dist}
BuildArch: noarch
Summary: Canonical source for classifiers on PyPI
License: Apache-2.0
URL: https://github.com/pypa/trove-classifiers/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Classifiers categorize projects per PEP 301. Use this package to
validate classifiers in packages for PyPI upload or download.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-trove-classifiers
Summary: Canonical source for classifiers on PyPI
Requires: python3
Provides: python3-trove-classifiers = %{epoch}:%{version}-%{release}
Provides: python3dist(trove-classifiers) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-trove-classifiers = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(trove-classifiers) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-trove-classifiers = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(trove-classifiers) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-trove-classifiers
Classifiers categorize projects per PEP 301. Use this package to
validate classifiers in packages for PyPI upload or download.

%files -n python%{python3_version_nodots}-trove-classifiers
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-trove-classifiers
Summary: Canonical source for classifiers on PyPI
Requires: python3
Provides: python3-trove-classifiers = %{epoch}:%{version}-%{release}
Provides: python3dist(trove-classifiers) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-trove-classifiers = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(trove-classifiers) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-trove-classifiers = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(trove-classifiers) = %{epoch}:%{version}-%{release}

%description -n python3-trove-classifiers
Classifiers categorize projects per PEP 301. Use this package to
validate classifiers in packages for PyPI upload or download.

%files -n python3-trove-classifiers
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-trove-classifiers
Summary: Canonical source for classifiers on PyPI
Requires: python3
Provides: python3-trove-classifiers = %{epoch}:%{version}-%{release}
Provides: python3dist(trove-classifiers) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-trove-classifiers = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(trove-classifiers) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-trove-classifiers = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(trove-classifiers) = %{epoch}:%{version}-%{release}

%description -n python3-trove-classifiers
Classifiers categorize projects per PEP 301. Use this package to
validate classifiers in packages for PyPI upload or download.

%files -n python3-trove-classifiers
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
