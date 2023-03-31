Name:		texlive-genealogytree
Version:	62759
Release:	2
Summary:	Pedigree and genealogical tree diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/genealogytree
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genealogytree.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/genealogytree.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Pedigree and genealogical tree diagrams are proven tools to
visualize genetic and relational connections between
individuals. The naming ("tree") derives from historical family
diagrams. However, even the smallest family entity consisting
of two parents and several children is hardly a 'mathematical'
tree -- it is a more general graph. The package provides a set
of tools to typeset genealogical trees (i.e., to typeset a set
of special graphs for the description of family-like
structures). The package uses an autolayout algorithm which can
be customized, e. g., to prioritize certain paths.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/genealogytree
%doc %{_texmfdistdir}/doc/latex/genealogytree

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
