Name:		texlive-bilingualpages
Version:	59643
Release:	2
Summary:	Typeset two columns in parallel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bilingualpages
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bilingualpages.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bilingualpages.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a simple wrapper for the paracol package for setting
two-column parallel text.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bilingualpages
%doc %{_texmfdistdir}/doc/latex/bilingualpages

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
