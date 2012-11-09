Summary:	Pattern Tools
Name:		pattern-tools
Version:	001
Release:	1
License:	GPLv2
Group:		System/Base
URL:		http://www.tizen.org
Source:		%{name}-%{version}.tar.bz2
Requires:  libxslt
Requires: python-yaml
Requires: python-lxml

%description tools
Tools for managing package groups and patterns.


%description
Pattern Tools

%prep
%setup -q

%build
make 

%install
%make_install


%files tools
%{_bindir}/merge-patterns
%{_datadir}/package-groups/stylesheets/*.xsl
