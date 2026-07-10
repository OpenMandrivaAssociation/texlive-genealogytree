%global tl_name genealogytree
%global tl_revision 79393

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4.1
Release:	%{tl_revision}.1
Summary:	Pedigree and genealogical tree diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/genealogytree
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/genealogytree.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/genealogytree.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Pedigree and genealogical tree diagrams are proven tools to visualize
genetic and relational connections between individuals. The naming
("tree") derives from historical family diagrams. However, even the
smallest family entity consisting of two parents and several children is
hardly a 'mathematical' tree -- it is a more general graph. The package
provides a set of tools to typeset genealogical trees (i.e., to typeset
a set of special graphs for the description of family-like structures).
The package uses an autolayout algorithm which can be customized, e. g.,
to prioritize certain paths.

