Summary:	It's a GTK+ interface to mysql/postgresql databases
Summary(pl):	Interfejs GTK+ do baz danych mysql/postgresql
Name:		dbui
Version:	0.4.0
Release:	1
License:	GPL
Group:		Applications/Databases/Interfaces
Source0:	http://spyder.virtualbeer.net/dbui/%{name}-%{version}.tar.gz
# Source0-md5:	962828bfc9bdb64697111624090bcfef
URL:		http://spyder.virtualbeer.net/dbui/
BuildRequires:	gtk+-devel
BuildRequires:	mysql-devel
# BuildRequires:	postgresql-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's a GTK+ interface to mysql/postgresql databases. You might say a
database editor. It's still in its very early stages but you can fully
search, update, add, and delete any mysql/postgresql database.

%description -l pl
To jest interfejs GTK+ do baz danych mysql/postgresql. Mo¿na go nazwaæ
edytorem baz danych. Nadal jest we wstêpnym stadium rozwoju, ale mo¿na
ju¿ przeszukiwaæ, uaktualniaæ, dodawaæ i usuwaæ z baz
mysql/postgresql.

%package mysql
Summary:	dbui linked with mysql
Summary(pl):	dbui skonsolidowane z mysql
Requires:	%{name} = %{version}
Group:		Applications/Databases/Interfaces

%description mysql
dbui linked with mysql.

%description mysql -l pl
dbui skonsolidowane z mysql.

%package postgresql
Summary:	dbui linked with postgresql
Summary(pl):	dbui skonsolidowane z postgresql
Requires:	%{name} = %{version}
Group:		Applications/Databases/Interfaces

%description postgresql
dbui linked with postgresql.

%description postgresql -l pl
dbui skonsolidowane z postgresql.

%prep
%setup  -q

%build
%{__make} -f Makefile.mysql
mv -f dbui dbui.mysql

#due to incompatibility with latest postgres libraries it doesn't compile
#correctly
# %{__make} -f Makefile.postgres
# mv -f dbui dbui.postgresql

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install dbui.mysql $RPM_BUILD_ROOT%{_bindir}
# install dbui.postgresql $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dbui.mysql

# %files postgresql
# %defattr(644,root,root,755)
# %attr(755,root,root) %{_bindir}/dbui.postgresql
