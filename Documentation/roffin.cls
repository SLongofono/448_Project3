%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% roffin.cls (Review of Finance)
% Created by: Aptara
% Created Date: 22nd Sept 2008
% Format: LaTeX
%
% Suitcase: 
% -------------------
% AMS/PS Screen Fonts
% CM/PS Screen Fonts
% LaTeX screen fonts
% Mathtime Screen Fonts
%
% normalsize -- 11/13
% footnotesize -- 9/11
% small -- 9/11
% tiny -- 5/6
% large -- 12/14
% Large -- 14/18
% LARGE -- 17/22
% huge -- 20/25
% Huge -- 25/30
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{roffin}[2008/09/22 v1.0 Standard LaTeX document class for Oxford Journals]
%
\newif\iffigcenter\global\figcenterfalse
\newif\ifdraft
\newdimen\draftrule
\newdimen\trimrule
\draftrule0pt
\trimrule.0pt
%
%
\@twosidetrue\@mparswitchtrue\@twocolumnfalse
%
\DeclareOption{manuscript}{\renewcommand{\baselinestretch}{2}}
\DeclareOption{figcenter}{\global\figcentertrue}
\DeclareOption{draft}{\setlength\overfullrule{5pt}\draftrule.25pt\drafttrue}
\DeclareOption{final}{\setlength\overfullrule{0pt}}
\ExecuteOptions{final}
\ProcessOptions
%
\newcommand\contentsname{Contents}
\newcommand\listfigurename{List of Figures}
\newcommand\listtablename{List of Tables}
\newcommand\bibname{References}
\newcommand\indexname{Index}
\newcommand\figurename{Fig.}
\newcommand\tablename{Table}
\newcommand\partname{Part}
\newcommand\chaptername{Chapter}
\newcommand\appendixname{Appendix}
%
\newcommand\today{\ifcase\month\or
  January\or February\or March\or April\or May\or June\or
  July\or August\or September\or October\or November\or December\fi
  \space\number\day, \number\year}
%
\newcount\minute
\newcount\hour
\def\currenttime{%
     \minute\time
     \hour\minute
     \divide\hour60
     \the\hour:\multiply\hour60\advance\minute-\hour\the\minute}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Boxes & Dimensions %%%%%%%%%%%%%%%%%%%%%
%
%
\newdimen\trimwidth
\newdimen\trimheight
\newdimen\typewidth
\newdimen\typeheight
%
\newdimen\tempdimen
\newdimen\normaltextheight
\newskip\normalbaselineskip
\newdimen\blindfoliodrop
%
\newdimen\enumdim
\newdimen\figheight
\newdimen\figwidth
\newdimen\tabledim
\newskip\tableleftskip
\newskip\tablerightskip
%
\newdimen\mathindent
\newdimen\emathindent
\newdimen\bibindent
%
\newbox\tempbox
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% End Boxes & Dimensions %%%%%%%%%%%%%%%%%
%
\def\mdash{{---}}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Fonts %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%% headings
\def\rhfont{\fontsize{8}{11}\selectfont\capsshape}
\def\RHfont{\fontsize{8}{9}\selectfont}
\def\foliofont{\fontsize{11}{11}\selectfont}
\def\dropfoliofont{\fontsize{8}{11}\selectfont}
\def\cpyinfofont{\fontsize{8}{9}\selectfont}
%% chapter
\def\sptitlefont{\fontsize{14.5}{15}\selectfont\itshape\rightskip0pc plus1fill}
\def\titlefont{\fontsize{17}{23}\selectfont\raggedright\mathversion{normal}}
\def\subtitlefont{}%\fontsize{16}{18}\selectfont\bfseries\rightskip0pc plus1fill\mathversion{bold}}
\def\authorfont{\fontsize{11}{13}\selectfont\capsshape\rightskip0pc plus1fill}
\def\affilfont{\fontsize{9}{13}\selectfont\itshape\rightskip0pt plus1fill}
\def\abstractfont{\fontsize{9}{11}\selectfont}
\def\keywordsfont{\fontsize{9}{11}\selectfont}
%% section
\def\sectionfont{\fontsize{11}{13}\selectfont\bfseries\rightskip0pc plus1fill\mathversion{bold}}
\def\subsectionfont{\fontsize{9}{10}\selectfont\capsshape\rightskip0pc plus1fill}
\def\subsubsectionfont{\fontsize{11}{13}\selectfont\itshape}
\def\paragraphfont{\fontsize{10}{11}\selectfont\itshape}%
\def\subparagraphfont{}%
\def\subsubparagraphfont{}%
%% figure
\iffigcenter%
  \def\figcaptionfont{\fontsize{9}{9.5}\selectfont}
\else%
  \def\figcaptionfont{\fontsize{9}{9.5}\selectfont\leftskip28pt}
\fi%
\def\figcaptionnumfont{\fontsize{9}{9.5}\selectfont\itshape}
%% table
\def\tablefont{\fontsize{8}{10}\selectfont}%\leftskip\tableleftskip\rightskip\tablerightskip}% 
\def\tablecaptionfont{\fontsize{9}{11}\selectfont\leftskip\tableleftskip\rightskip\tablerightskip}% 
\def\tablecaptionnumfont{\fontsize{9}{11}\selectfont\itshape}% 
\def\TCHfont{\fontsize{8}{10}\selectfont}%
\def\TSCHfont{\fontsize{8}{10}\selectfont}%
\def\tabnotefont{\fontsize{8}{10}\selectfont\leftskip\tableleftskip\rightskip\tablerightskip}% 
%% box
\def\boxfont{\fontsize{8}{9}\selectfont}%
\def\boxcaptionfont{\fontsize{8}{9}\selectfont}% 
\def\boxcaptionnumfont{\fontsize{8}{9}\selectfont\bfseries}% 
%% BM
\def\indexfont{\fontsize{8}{9}\selectfont\raggedright}
\def\bibliofont{\fontsize{9}{11}\selectfont}
%
\def\listfont{}
\def\listdevicefont{}
\def\extractfont{\fontsize{9}{10}\selectfont\leftskip1pc\rightskip\leftskip}
%
%%%%%%%%%%%%%%%%%%%%%%%%% Fonts %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\@xvpt{15}
\def\@xviiipt{18}
\def\@xxivpt{24}
%
\normalbaselineskip11pt
%
\renewcommand\normalsize{%
   \@setfontsize\normalsize\@xipt{13}
   \abovedisplayskip 5.5\p@ \@plus2\p@ \@minus.5\p@
   \abovedisplayshortskip \abovedisplayskip
   \belowdisplayshortskip \abovedisplayskip
   \belowdisplayskip \abovedisplayskip
   \let\@listi\@listI}
\def\biggg#1{{\hbox{$\left#1\vbox to20.5\p@{}\right.\n@space$}}}
\def\Biggg#1{{\hbox{$\left#1\vbox to23.5\p@{}\right.\n@space$}}}
\normalsize
%
\newcommand\small{%
   \@setfontsize\small\@ixpt{11}%
   \abovedisplayskip 8.5\p@ \@plus3\p@ \@minus4\p@
   \abovedisplayshortskip \z@ \@plus2\p@
   \belowdisplayshortskip 4\p@ \@plus2\p@ \@minus2\p@
   \def\@listi{\leftmargin\leftmargini
               \topsep 4\p@ \@plus2\p@ \@minus2\p@
               \parsep 2\p@ \@plus\p@ \@minus\p@
               \itemsep \parsep}%
   \belowdisplayskip \abovedisplayskip
   \setSmallDelims}
%
\def\setSmallDelims{%
\def\big##1{{\hbox{$\left##1\vbox to7.5\p@{}\right.\n@space$}}}%
\def\Big##1{{\hbox{$\left##1\vbox to10.5\p@{}\right.\n@space$}}}%
\def\bigg##1{{\hbox{$\left##1\vbox to13.5\p@{}\right.\n@space$}}}%
\def\Bigg##1{{\hbox{$\left##1\vbox to16.5\p@{}\right.\n@space$}}}%
\def\biggg##1{{\hbox{$\left##1\vbox to19.5\p@{}\right.\n@space$}}}%
\def\Biggg##1{{\hbox{$\left##1\vbox to22.5\p@{}\right.\n@space$}}}%
}
%
\newcommand\footnotesize{%
   \@setfontsize\footnotesize\@ixpt{11}%
   \abovedisplayskip 6\p@ \@plus2\p@ \@minus4\p@
   \abovedisplayshortskip \z@ \@plus\p@
   \belowdisplayshortskip 3\p@ \@plus\p@ \@minus2\p@
   \def\@listi{\leftmargin\leftmargini
               \topsep 3\p@ \@plus\p@ \@minus\p@
               \parsep 2\p@ \@plus\p@ \@minus\p@
               \itemsep \parsep}%
   \belowdisplayskip \abovedisplayskip
   \setFootnotesizeDelims}
%
\def\setFootnotesizeDelims{%
\def\big##1{{\hbox{$\left##1\vbox to6.5\p@{}\right.\n@space$}}}%
\def\Big##1{{\hbox{$\left##1\vbox to9.5\p@{}\right.\n@space$}}}%
\def\bigg##1{{\hbox{$\left##1\vbox to12.5\p@{}\right.\n@space$}}}%
\def\Bigg##1{{\hbox{$\left##1\vbox to15.5\p@{}\right.\n@space$}}}%
\def\biggg##1{{\hbox{$\left##1\vbox to18.5\p@{}\right.\n@space$}}}%
\def\Biggg##1{{\hbox{$\left##1\vbox to21.5\p@{}\right.\n@space$}}}%
}
%   
\newcommand\scriptsize{\@setfontsize\scriptsize\@viipt\@viiipt}
\newcommand\tiny{\@setfontsize\tiny\@vpt\@vipt}
\newcommand\large{\@setfontsize\large\@xiipt{14}}
\newcommand\Large{\@setfontsize\Large\@xivpt{18}}
\newcommand\LARGE{\@setfontsize\LARGE\@xviipt{22}}
\newcommand\huge{\@setfontsize\huge\@xxpt{25}}
\newcommand\Huge{\@setfontsize\Huge\@xxvpt{30}}
%
%%%%%%%  For Times family  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\DeclareOldFontCommand{\rm}{\normalfont\rmfamily}{\mathrm}
\DeclareOldFontCommand{\sf}{\normalfont\sffamily}{\mathsf}
\DeclareOldFontCommand{\tt}{\normalfont\ttfamily}{\mathtt}
\DeclareOldFontCommand{\bf}{\normalfont\bfseries}{\mathbf}
\DeclareOldFontCommand{\it}{\normalfont\itshape}{\mathit}
\DeclareOldFontCommand{\sl}{\normalfont\slshape}{\@nomath\sl}
\DeclareOldFontCommand{\sc}{\normalfont\scshape}{\@nomath\sc}
\DeclareOldFontCommand{\bi}{\bfseries\itshape}{\bfseries\itshape}
\newcommand{\cal}{\protect\pcal}
\newcommand{\pcal}{\@fontswitch{\relax}{\mathcal}}
\newcommand{\mit}{\protect\pmit}
\newcommand{\pmit}{\@fontswitch{\relax}{\mathnormal}}
%
\def\capsdefault{caps}% all CAPS
\DeclareRobustCommand\capsshape
        {\not@math@alphabet\capsshape\mathrm
         \fontshape\capsdefault\selectfont}
%
\def\blkdefault{blk}%
\DeclareRobustCommand\blkseries
        {\not@math@alphabet\blkseries\relax
         \fontseries\blkdefault\selectfont}
%
% if base font is changed them Change MTMI, MTMIB
%
%
\DeclareFontFamily{OT1}{ams}{}
\DeclareFontShape{OT1}{ams}{m}{n}{ <-> msam10 }{}
\DeclareFontShape{OT1}{ams}{m}{it}{ <-> msam10 }{}
\DeclareFontShape{OT1}{ams}{bx}{n}{ <-> msbm10 }{}
\DeclareFontShape{OT1}{ams}{bx}{it}{ <-> msbm10 }{}
%
\def\encodingdefault{OT1}%
\fontencoding{OT1}%
%
%
\def\encodingdefault{OT1}%
\fontencoding{OT1}%
%%
%
\DeclareFontShape{OMS}{cmsy}{m}{n}{ <-> cmsy10 }{}
\DeclareFontShape{OMS}{cmsy}{b}{n}{ <-> cmbsy10 }{}
\def\cal{\mathcal}
%
% Remove the following definitions if you use CM fonts for math
%
%
\font\foot= cmsy10 at 6pt
\def\SS{\hbox{\foot\char'170}}%
%
%\def\qvec{\mathaccent"017E}
\def\qvec{\mathaccent"0245}
\def\vec#1{\mathaccent"0245{#1}}
\def\lhd{\mathbin{< \hbox to -.43em{}\hbox{\vrule
      \@width .065em \@height .55em \@depth .05em}\hbox to .2em{}}}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Bold Math %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\boldmath{\mathversion{bold}}
\def\bm#1{\mathchoice
          {\mbox{\boldmath$\displaystyle#1$}}%
          {\mbox{\boldmath$#1$}}%
          {\mbox{\boldmath$\scriptstyle#1$}}%
          {\mbox{\boldmath$\scriptscriptstyle#1$}}}
%
% define blackboard font
\def\bb#1{\mathchoice
	{\mbox{\fontfamily{ams}\fontsize{\tf@size}{\tf@size}\selectfont\bf#1}}%
	{\mbox{\fontfamily{ams}\fontsize{\tf@size}{\tf@size}\selectfont\bf#1}}%
	{\mbox{\fontfamily{ams}\fontsize{\sf@size}{\sf@size}\selectfont\bf#1}}%
	{\mbox{\fontfamily{ams}\fontsize{\ssf@size}{\ssf@size}\selectfont\bf#1}}}
%
\DeclareMathAlphabet{\mathbb}{OT1}{ams}{bx}{n}
\SetMathAlphabet\mathbb{normal}{OT1}{ams}{bx}{n}
\SetMathAlphabet\mathbb{bold}{OT1}{ams}{bx}{n}
\def\bb{\mathbb}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% End Fonts %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Parameters %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\setlength\trimheight{297mm}%
\setlength\trimwidth{210mm}%
%
\setlength\typeheight{46pc}
\setlength\typewidth{30pc}
%
\setlength\textheight{44pc}
\setlength\normaltextheight{\textheight}
\setlength\textwidth{30pc}
%
\setlength\topmargin{146pt}%
\setlength\oddsidemargin{118.5pt}%
\setlength\evensidemargin\trimwidth
\addtolength\evensidemargin{-\textwidth}
\addtolength\evensidemargin{-\oddsidemargin}
%\addtolength\oddsidemargin{3pc}
%
\setlength\headheight{6\p@}% 
\setlength\headsep   {19pt}% 
\setlength\topskip   {7.6\p@}
\setlength\splittopskip   {\topskip}
%
\setlength\footskip{26.5pt}%
\setlength\maxdepth{4\p@}
%
\blindfoliodrop\trimheight
\advance\blindfoliodrop-\typeheight
\advance\blindfoliodrop-\topmargin
\advance\blindfoliodrop-\footskip
\advance\blindfoliodrop18pt
%
\setlength\parindent{1em}
%
\setlength\marginparwidth {2pc}
\setlength\marginparsep{7\p@}
\setlength\marginparpush{5\p@}
%
\setlength\footnotesep{6.65\p@}
\setlength{\skip\footins}{12\p@ \@plus 8\p@ \@minus 8\p@}%
\skip\@mpfootins = \skip\footins
%
\setlength\floatsep    {12\p@ \@plus 2\p@ \@minus 2\p@}
\setlength\textfloatsep{13\p@ \@plus 2\p@ \@minus 4\p@}
\setlength\intextsep   {12\p@ \@plus 2\p@ \@minus 2\p@}
\setlength\dblfloatsep    {12\p@ \@plus 2\p@ \@minus 2\p@}
\setlength\dbltextfloatsep{20\p@ \@plus 2\p@ \@minus 4\p@}
\setlength\@fptop{0\p@}
\setlength\@fpsep{8\p@ \@plus 1fil}
\setlength\@fpbot{0\p@ \@plus 1fil}
\setlength\@dblfptop{0\p@}
\setlength\@dblfpsep{8\p@ \@plus 1fil}
\setlength\@dblfpbot{0\p@ \@plus 1fil}
%
\setlength\partopsep{0pt}
\setlength\lineskip{1\p@}%
\setlength\normallineskip{1\p@}%
\setlength\parskip{\z@}%{0\p@ \@plus \p@}
\sloppy
\clubpenalty10000
\widowpenalty10000%
\@lowpenalty   51
\@medpenalty  151
\@highpenalty 301
%
\@beginparpenalty -\@lowpenalty
\@endparpenalty   -\@lowpenalty
\@itempenalty     -\@lowpenalty
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% End Parameters %%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Article Title  %%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\cleardoublepage{\clearpage\if@twoside \ifodd\c@page\else
    \hbox{}\thispagestyle{empty}\newpage\if@twocolumn\hbox{}\newpage\fi\fi\fi}
%
\def\sptitle#1{\gdef\@sptitle{{}#1}}
\sptitle{}
\def\title#1{\gdef\@title{#1}}
\def\@subtitle{}
\def\subtitle#1{\gdef\@subtitle{#1}}
\def\author#1{\gdef\@author{#1}}\author{}
\def\@affil{}
\def\affil#1{\protected@xdef\@affil{\ifx\@affil\@empty\else\@affil; \fi#1}}%\affil{}
\def\received#1{\xdef\@received{#1}}\def\@received{}
\def\revised#1{\xdef\@revised{#1}}\def\@revised{}
\def\accepted#1{\xdef\@accepted{#1}}\def\@accepted{}
%
\newcount\articlecount%
\newif\ifmergenewarticle%
\global\mergenewarticlefalse%
\def\mergearticle{\global\mergenewarticletrue}
\gdef\Inarticletitle{no}%

\newcommand\maketitle{\par%
  \gdef\Inarticletitle{yes}%
    \begingroup%
      \long\def\@makefntext##1{\let\doPar\relax\noindent{##1}}%
      \@maketitle%
      \thispagestyle{plain}%
    \@thanks%
    \endgroup%
  \gdef\@sptitle{}%
  \gdef\@thanks{}%
  \renewcommand\thefootnote{\arabic{footnote}}%
  \gdef\@title{}}
%
\def\@maketitle{%
  \clearpage%
  \null%
  \bgroup%
  \parindent0pt%
  \ifx\@sptitle\empty\vspace*{-15pt}\else\par\vspace*{13pt}\noindent{\sptitlefont\@sptitle\par\vskip24pt}\fi%
  \ifx\@title\empty\else{\vspace*{-18.5pt}\titlefont{\@title\vphantom{pg}}\par}\fi%
  \ifx\@subtitle\@empty\else\vskip10pt{\subtitlefont\@subtitle}\fi%
  \ifx\@author\empty\else\vskip19pt\noindent{\authorfont\@author\par}\fi%
  \ifx\@affil\empty\else\vskip0pt\noindent{\affilfont\@affil\par}\fi%
  \vskip16.5pt%
  \egroup}
%
\def\@meargedmaketitle{%
  \null\bgroup%
  \ifmergenewarticle%
    \parindent0pt%
    \vskip-16.5pt\par%
    \noindent{\vrule height.5pt width\hsize depth0pt}\par\vskip24.5pt%
  \else%
    \clearpage%
    \parindent0pt%
    \vspace*{-26.75pt}%
  \fi%
  {\vbox{\hsize\textwidth%0
     \hbox{{\RHfont%
       \ifx\@jname\@empty\else\@jname\fi%
       \ifx\@jyear\@empty\else\unskip\ (\@jyear)\fi%
       \ifx\@jvol\@empty\else\ \@jvol\unskip{:}\fi%
       \ifx\f@page\@empty\else\ \f@page\fi%
       \ifx\l@page\@empty\else--\l@page\fi%
       }}\par%
     \hbox{{\RHfont\ifx\@doi\@empty\else{doi:}\ \@doi\fi}}\par%
     \hbox{{\RHfont\ifx\@accessdate\@empty\else\@accessdate\fi}}%
  }\par\vskip24pt}%
  {\titlefont{\@title\vphantom{pg}}\par}%
  \ifx\@authors\empty\else\vskip24.25pt\noindent{\authorfont\@authors\par}\fi%
  \ifx\@affils\empty\else\vskip16pt\noindent{\affilfont\@affils\par}\fi%
  \vskip25.5pt%
  \egroup}
%%
\def\endarticlerule{\par\vskip-4pt%
  \noindent\hspace*{-20.5pc}{\vrule height.5pt width\textwidth depth0pt}%
}
%
%=========================================================
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  End Article Title  %%%%%%%%%%%%%%%%%%%%%
%
\newenvironment{abstract}{\par\addvspace{0pt}%
                \noindent\abstractfont{\bfseries Abstract.}\enspace%\par\vskip2pt%
                \abstractfont%\ignorespaces%
               }{\par\addvspace{17pt}}
%
\gdef\YES{yes}
\gdef\NO{no}
\gdef\firstkey{yes}
\def\keywords@type{}%
\def\keyword#1{\ifx\firstkey\YES#1\else\unskip; #1\fi\gdef\firstkey{no}}
\newenvironment{keywords}{\par\addvspace{0pt}
                \noindent\keywordsfont\ignorespaces {\bfseries Keywords:}\ 
               }{\par\addvspace{17pt}}
%
\def\jelcode#1{\par\addvspace{0pt}\noindent\keywordsfont{\itshape JEL Classification:}\enspace #1\par\addvspace{17pt}}
%
\newbox\abbrebox
\newenvironment{abbre}{\hsize\textwidth%
		\global\setbox\abbrebox\vbox\bgroup\par\addvspace{14pt}\absfont\noindent{\bi Abbre{v}iations:}\ \ignorespaces%
  }{%
		\egroup}
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Sectioning commands  %%%%%%%%%%%%%%%%%%%%
%
\setcounter{secnumdepth}{3}
\newcounter {part}
\newcounter {chapter}
\newcounter {section}[chapter]
\newcounter {subsection}[section]
\newcounter {subsubsection}[subsection]
\newcounter {paragraph}[subsubsection]
\newcounter {subparagraph}[paragraph]
\renewcommand\thepart          {\Roman{part}}
\renewcommand\thechapter       {\arabic{chapter}}
\renewcommand\thesection       {\arabic{section}.}
\renewcommand\thesubsection    {\thesection\arabic{subsection}}
\renewcommand\thesubsubsection {\thesubsection .\arabic{subsubsection}}
\renewcommand\theparagraph     {\thesubsubsection.\arabic{paragraph}}
\renewcommand\thesubparagraph  {\theparagraph.\arabic{subparagraph}}
%
\def\@seccntformat#1{\csname the#1\endcsname\hskip .5em}
%
\def\@subseccntformat#1{\csname the#1\endcsname\hskip .5em}
%
\newcommand\section{\@startsection {section}{1}{\z@}{-18pt \@plus -2pt \@minus -.2pt}{11pt}{\sectionfont}}%
\newcommand\subsection{\@startsection{subsection}{2}{\z@}{-16pt \@plus -2pt \@minus -.2pt}{11pt}{\subsectionfont}}%
\newcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}{-11pt \@plus -2pt \@minus -.2pt}{8pt}{\subsubsectionfont}}%
\newcommand\paragraph{\@startsection{paragraph}{4}{1em}{-0.001pt}{-1em}{\paragraphfont}}%
\newcommand\subparagraph{\@startsection{subparagraph}{5}{\parindent}{-0.001pt}{-1em}{\subparagraphfont}}%
\newcommand\subsubparagraph{\@startsection{subsubparagraph}{6}{\parindent}{-19pt \@plus -2pt \@minus -.2pt}{-1em}{\subsubparagraphfont}}%
%
%
\def\@sect#1#2#3#4#5#6[#7]#8{%
  \ifnum #2>\c@secnumdepth%
    \let\@svsec\@empty%
  \else%
    \refstepcounter{#1}%
    \let\@@protect\protect
    \def\protect{\noexpand\protect\noexpand}%
    \edef\@svsec{\@seccntformat{#1}}%
    \edef\@svsubsec{\@subseccntformat{#1}}
    \let\protect\@@protect%
  \fi
  \@tempskipa #5\relax%
  \ifdim \@tempskipa>\z@%
    \begingroup #6\relax%
    \noindent{\hskip #3\relax\ifnum#2=2\@svsubsec\else\@svsec\fi}% {\csname #1numfont\endcsname\@svsec}
              {\interlinepenalty \@M #8 \par}%
    \endgroup%
    \csname #1mark\endcsname{#7}\addcontentsline{toc}{#1}{\ifnum #2>\c@secnumdepth \else\protect\numberline{\csname the#1\endcsname}\fi
      #7}%
  \else%
    \def\@svsechd{#6\hskip #3\relax  %
      \@svsec #8\ifnum#2=3\else\ifnum#2=4\fi\fi\csname #1mark\endcsname{#7}%
      \addcontentsline{toc}{#1}{\ifnum #2>\c@secnumdepth \else\protect\numberline{\csname the#1\endcsname}\fi#7}}%
  \fi%
  \@xsect{#5}%
}
%
\def\@startsection#1#2#3#4#5#6{%
  \if@noskipsec \leavevmode \fi
  \par
  \@tempskipa #4\relax
  \@afterindenttrue
  \ifdim \@tempskipa <\z@
    \@tempskipa -\@tempskipa \@afterindentfalse
  \fi
  \if@nobreak
  \ifnum#2=2
    \vskip3pt%
  \fi
    \everypar{}
  \else
    \addpenalty\@secpenalty\addvspace\@tempskipa
  \fi
  \@ifstar
    {\@ssect{#3}{#4}{#5}{#6}}%
    {\@dblarg{\@sect{#1}{#2}{#3}{#4}{#5}{#6}}}}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  End Sectioning commands  %%%%%%%%%%%%%%%%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Lists %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\newskip\topsepi \topsepi6\p@ \@plus2\p@% \@minus.5\p@
\newskip\topsepii \topsepii2pt% \@plus1\p@ 
\newskip\topsepiii \topsepiii2pt% \@plus1\p@ 
\newskip\itemsepi \itemsepi0pt
\newskip\itemsepii \itemsepii0pt
\newskip\itemsepiii \itemsepiii0pt
\newdimen\LabelSep \LabelSep4.7pt
%
\def\@listI{\leftmargin\leftmargini
            \labelwidth\leftmargini
            \advance\labelwidth-\labelsep
            \parsep 0\p@%
            \topsep \topsepi
            \itemsep\itemsepi}%
\let\@listi\@listI
\@listi
\def\@listii {\leftmargin\leftmarginii
              \labelwidth\leftmarginii
              \advance\labelwidth-\labelsep
              \topsep\topsepii
              \parsep 0pt
              \itemsep\itemsepii}
\def\@listiii {\leftmargin\leftmarginiii
              \labelwidth\leftmarginiii
              \advance\labelwidth-\labelsep
              \topsep\topsepiii
              \parsep 0pt
              \itemsep\itemsepiii}
\def\@listiv {\leftmargin\leftmarginiv
              \labelwidth\leftmarginiv
              \advance\labelwidth-\labelsep}
\def\@listv  {\leftmargin\leftmarginv
              \labelwidth\leftmarginv
              \advance\labelwidth-\labelsep}
\def\@listvi {\leftmargin\leftmarginvi
              \labelwidth\leftmarginvi
              \advance\labelwidth-\labelsep}
%
\setlength\leftmargini  {2.5em}
\setlength\leftmarginii  {2.2em}
\setlength\leftmarginiii {1.87em}
\setlength\leftmarginiv  {1.7em}
\setlength\leftmarginv  {1em}
\setlength\leftmarginvi {1em}
\setlength\leftmargin    {\leftmargini}
%
\setlength  \labelsep  {\LabelSep}
\setlength  \labelwidth{\leftmargini}
\addtolength\labelwidth{-\labelsep}
%
\renewcommand\theenumi{\arabic{enumi}}
\renewcommand\theenumii{\alph{enumii}}
\renewcommand\theenumiii{\roman{enumiii}}
\renewcommand\theenumiv{\Alph{enumiv}}
\newcommand\labelenumi{\theenumi.}
\newcommand\labelenumii{\theenumii.}
\newcommand\labelenumiii{\theenumiii.}
\newcommand\labelenumiv{\theenumiv.}
\renewcommand\p@enumii{\theenumi}
\renewcommand\p@enumiii{\theenumi(\theenumii)}
\renewcommand\p@enumiv{\p@enumiii\theenumiii}
\font\lcir = lcircle10 at 12pt
\newcommand\bulls{\raise1.5pt\hbox{\lcir\char'162}}
\def\textbullet{\leavevmode\raise2pt\hbox{\hskip2pt\bulls}}
\def\textendash{{\bf--}}
\def\textasteriskcentered{\leavevmode\raise-1.5pt\hbox{*}}
\def\textperiodcentered{\leavevmode\raise1.5pt\hbox{\bulls}}
\newcommand\labelitemi{\textbullet}
\newcommand\labelitemii{\normalfont\bfseries \textendash}
\newcommand\labelitemiii{\textasteriskcentered}
\newcommand\labelitemiv{\textperiodcentered}
%
\newenvironment{description}
               {\list{}{\labelwidth\z@ \itemindent-\leftmargin
                        \let\makelabel\descriptionlabel}}
               {\endlist}
\newcommand\descriptionlabel[1]{\hspace\labelsep
                                \normalfont\bfseries #1}
%
\newenvironment{verse}
               {\let\\=\@centercr
                \list{}{\itemsep      \z@
                        \itemindent   -1.5em%
                        \listparindent\itemindent
                        \rightmargin  \leftmargin
                        \advance\leftmargin 1.5em}%
                \item[]}
               {\endlist}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  End Lists %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Quotes %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\newenvironment{quote}{\list{}{\rightmargin\leftmargin}%
                \item[]}
               {\endlist}
%
%
\newenvironment{extract}{\par\addvspace{5.5pt plus2pt}%
      \extractfont%
	\noindent%
}{%
      \par\addvspace{5.5pt plus2pt}}
%
\def\leadintextfont{\itshape}
\def\leadintext#1{{\leadintextfont#1}\hskip2.5pt}%
%
\def\ackfont{\fontsize{8}{9}\selectfont}
\newenvironment{ack}{\par\addvspace{13pt}%
                     \noindent\ackfont\ignorespaces% {\itshape Acknowledgments.}\hskip1em
                    }{\par\addvspace{0pt}}
%%
\def\conflictfont{\fontsize{8}{9}\selectfont}
\def\conflict#1{\par\addvspace{14pt}%
  \noindent{\conflictfont#1\par}%
}

\def\methodsfont{\fontsize{9}{10.5}\selectfont}

\newenvironment{methods}{\par\vskip.5pt%
  \noindent\methodsfont\ignorespaces%
  }{\par}
%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  End Quotes %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\lhfont{\fontsize{10}{12}\selectfont\bfseries}
\def\lh#1{\par\addvspace{\baselineskip}\noindent{\lhfont#1\par}\vspace*{-5.9pt}}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Enumerate list %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\newskip\listtextleftmargin\listtextleftmargin 30.5pt%
\newskip\listtextleftmarginii\listtextleftmarginii0pt%
\newskip\listtextleftmarginiii\listtextleftmarginiii0pt%
\newskip\listtextrightmargin\listtextrightmargin0pt%
\newskip\listlabelleftskip \listlabelleftskip19pt%
\newskip\listlabelleftskipii \listlabelleftskipii0pt%
\newskip\listlabelleftskipiii \listlabelleftskipiii0pt%
\newskip\abovelistskipi\abovelistskipi5.5pt% 
\newskip\belowlistskipi\belowlistskipi5.5pt% 
\newskip\abovelistskipii\abovelistskipii0pt% 
\newskip\belowlistskipii\belowlistskipii0pt% 
\newskip\abovelistskipiii\abovelistskipiii0pt%
\newskip\belowlistskipiii\belowlistskipiii0pt%
\newskip\labelsepi \labelsepi4.4pt
\newskip\labelsepii \labelsepii5.2pt
\newskip\labelsepiii \labelsepiii\z@
\newdimen\enumdimwd
\newif\iflabelrightalign\labelrightaligntrue
%
\def\listdevicefonti{}
\def\listdevicefontii{}
\def\listdevicefontiii{}
\def\listfont{}
\def\textlistlabel{}
%
\def\enummax#1{%
  \labelsep\csname labelsep\romannumeral\the\@enumdepth\endcsname
  \ifdim\listtextleftmargin>\z@\labelsepi0pt\fi
  \ifdim\listtextleftmarginii>\z@\labelsepii0pt\fi
  \ifdim\listtextleftmarginiii>\z@\labelsepiii0pt\fi
  \setbox\tempbox\hbox{\csname listdevicefont\romannumeral\the\@enumdepth\endcsname#1\hskip\labelsep}%
  \enumdim\wd\tempbox
  \setbox\tempbox\hbox{\csname listdevicefont\romannumeral\the\@enumdepth\endcsname#1}%
  \enumdimwd\wd\tempbox
  \expandafter\global\csname leftmargin\romannumeral\the\@enumdepth\endcsname\enumdim
  \ifdim\listtextleftmargin>\z@
     \leftmargini\listtextleftmargin
     \ifdim\listlabelleftskip>\z@
        \advance\leftmargini-\listlabelleftskip
     \fi  
  \fi
  \ifdim\listtextleftmarginii>\z@
     \leftmarginii\listtextleftmarginii
     \ifdim\listlabelleftskipii>\z@
        \advance\leftmarginii-\listlabelleftskipii
     \fi  
  \fi
  \ifdim\listtextleftmarginiii>\z@
     \leftmarginiii\listtextleftmarginiii
     \ifdim\listlabelleftskipiii>\z@
        \advance\leftmarginiii-\listlabelleftskipiii
     \fi  
  \fi
  \ifdim\listlabelleftskip>\z@
     \advance\leftmargini\listlabelleftskip
  \fi
  \ifdim\listlabelleftskipii>\z@
     \advance\leftmarginii\listlabelleftskipii
  \fi
    \ifdim\listlabelleftskipiii>\z@
     \advance\leftmarginiii\listlabelleftskipiii
  \fi}
%
\enummax{1.}
%
\def\enumerate{\@ifnextchar[{\@enumerate}{\@enumerate[\csname label\@enumctr\endcsname]}}%% 
%
\def\@enumerate[#1]{\par
      \ifnum \@enumdepth >3 \@toodeep\else
      \advance\@enumdepth\@ne
      \edef\@enumctr{enum\romannumeral\the\@enumdepth}%
      \setcounter{\@enumctr}{1}\enummax{#1}%
      \list
          {\csname label\@enumctr\endcsname}{\usecounter{\@enumctr}%
      \topsep\csname abovelistskip\romannumeral\the\@enumdepth\endcsname
      \itemsep\csname itemsep\romannumeral\the\@enumdepth\endcsname
      \listfont %
      \ifnum \@enumdepth=1 
         \rightmargin\listtextrightmargin
         \advance\rightmargin\rightskip
         \advance\leftmargin\leftskip
         \tempdimen\leftmargini
         \advance\tempdimen-\labelsep
         \def\makelabel##1{\hbox to \tempdimen{\hskip\listlabelleftskip{\csname listdevicefont\romannumeral\the\@enumdepth\endcsname\hbox to \enumdimwd{\iflabelrightalign\hss\fi\textlistlabel##1}}}}%
      \else
      \ifnum \@enumdepth=2
         \tempdimen\leftmarginii
         \advance\tempdimen-\labelsep
         \def\makelabel##1{\hbox to \tempdimen{\hskip\listlabelleftskipii{\csname listdevicefont\romannumeral\the\@enumdepth\endcsname\hbox to \enumdimwd{\iflabelrightalign\hss\fi##1}}}}%
      \else
         \ifnum \@enumdepth=3
         \tempdimen\leftmarginiii
         \advance\tempdimen-\labelsep
         \def\makelabel##1{\hbox to \tempdimen{\hskip\listlabelleftskipiii{\csname listdevicefont\romannumeral\the\@enumdepth\endcsname\hbox to \enumdimwd{\iflabelrightalign\hss\fi##1}}}}%
     \else
         \def\makelabel##1{\hss\llap{\csname listdevicefont\romannumeral\the\@enumdepth\endcsname##1}}%
      \fi\fi
      \fi}\fi}
%
\def\endenumerate{\@topsepadd\csname belowlistskip\romannumeral\the\@enumdepth\endcsname\endlist}%
%
\newenvironment{arabiclist}{%
  \def\theenumi{\arabic{enumi}}
  \def\theenumii{\arabic{enumii}}%
  \def\theenumiii{\arabic{enumiii}}%
  \def\theenumiv{\arabic{enumiv}}%
  \renewcommand\labelenumi{\theenumi.}
  \begin{enumerate}%
}{%
  \end{enumerate}}
%
\newenvironment{wherelist}{%
  \def\listdevicefonti{\upshape}
  \listtextleftmargin 0pt
  \abovelistskipi13\p@ plus2pt
  \belowlistskipi13\p@ plus2pt
  \begin{enumerate}%
}{%
  \end{enumerate}}
%
\newenvironment{romanlist}{%
  \def\theenumi{\roman{enumi}}
  \def\theenumii{\roman{enumii}}%
  \def\theenumiii{\roman{enumiii}}
  \def\theenumiv{\roman{enumiv}}%
  \renewcommand\labelenumi{(\theenumi)}
  \begin{enumerate}%
}{%
  \end{enumerate}}
%
\newenvironment{alphalist}{%
\listtextleftmargin 18pt
\listtextleftmarginii 18pt
\itemsepi3pt
\labelrightalignfalse
  \def\theenumi{\alph{enumi}}\def\theenumii{\alph{enumii}}%
  \def\theenumiii{\alph{enumiii}}\def\theenumiv{\alph{enumiv}}%
  \renewcommand\labelenumi{(\theenumi)}
  \begin{enumerate}%
}{%
  \end{enumerate}}
%
\newenvironment{Romanlist}{%
  \def\theenumi{\Roman{enumi}}\def\theenumii{\Roman{enumii}}%
  \def\theenumiii{\Roman{enumiii}}\def\theenumiv{\Roman{enumiv}}%
  \begin{enumerate}%
}{%
  \end{enumerate}}
%
\newenvironment{Alphalist}{%
  \def\theenumi{\Alph{enumi}}\def\theenumii{\Alph{enumii}}%
  \def\theenumiii{\Alph{enumiii}}\def\theenumiv{\Alph{enumiv}}%
  \begin{enumerate}%
}{%
  \end{enumerate}}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  unnumlist %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\newenvironment{unnumlist}{%
    \list{}{%
        \leftmargin18pt
        \itemindent-18pt
    \parsep0pt
    \itemsep0pt
    \partopsep0pt}
    \def\makelable##1{##1}%
}{%
    \endlist
}%
%
\def\webadd#1{\par\addvspace{3pt}{\fontfamily{Courier}\fontsize{9}{12}\selectfont\hskip18pt#1}}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%% itemize (bullet) %%%%%%%%%%%%%%%%%%%%%%%%%%
%
% define \itemizeiTopSep if it is different from \topsepi
%
\newdimen\itemleftmargin \itemleftmargin12pt%\z@ % won't be active in enumerate
\newdimen\itemlabelsep \itemlabelsep10.75\p@ % labelsep in itemize for all levels
%
\def\itemize{%
  \ifnum \@itemdepth >3 \@toodeep\else\ifnum\@enumdepth>0\@itemdepth\@enumdepth\fi \advance\@itemdepth \@ne
     \edef\@itemitem{labelitem\romannumeral\the\@itemdepth}%
     \list{\csname\@itemitem\endcsname}%
        {%
        \topsep\csname abovelistskip\romannumeral\the\@itemdepth\endcsname%\fi
        \itemsep\csname itemsep\romannumeral\the\@itemdepth\endcsname
        \labelsep\itemlabelsep
        \listfont
        \setbox\tempbox\hbox{\csname\@itemitem\endcsname}
        \csname leftmargin\romannumeral\the\@itemdepth\endcsname\wd\tempbox
        \advance\csname leftmargin\romannumeral\the\@itemdepth\endcsname\itemlabelsep
        \ifnum\@itemdepth=\@ne\ifnum\@enumdepth=0 % if not inside an enumerate
           \rightmargin\listtextrightmargin
           \advance\rightmargin\rightskip
           \advance\csname leftmargin\romannumeral\the\@itemdepth\endcsname\itemleftmargin
           \advance\leftmargini\leftskip
        \else
        \advance\csname leftmargin\romannumeral\the\@itemdepth\endcsname\itemleftmargin
           \advance\leftmarginii\leftskip
        \fi\fi
        \leftmargin\csname leftmargin\romannumeral\the\@itemdepth\endcsname
        \def\makelabel##1{\hss\llap{##1}}}
   \fi}%
%
\def\enditemize{%
\@topsepadd\csname belowlistskip\romannumeral\the\@itemdepth\endcsname%\fi
\endlist}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%% enumroman (i) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\newenvironment{bulletlist}{%
   \renewcommand\labelitemi{\textbullet}%
   \renewcommand\labelitemii{\textbullet}%
   \renewcommand\labelitemiii{\textbullet}%
   \renewcommand\labelitemiv{\textbullet}%
   \begin{itemize}
}{%
   \end{itemize}}
%
\newenvironment{hyphenlist}{%
   \renewcommand\labelitemi{\normalfont\bfseries \textendash}%
   \renewcommand\labelitemii{\normalfont\bfseries \textendash}%
   \renewcommand\labelitemiii{\normalfont\bfseries \textendash}%
   \renewcommand\labelitemiv{\normalfont\bfseries \textendash}%
   \begin{itemize}
}{%
   \end{itemize}}
%
\newenvironment{asterisklist}{%
   \renewcommand\labelitemi{\textasteriskcentered}%
   \renewcommand\labelitemii{\textasteriskcentered}%
   \renewcommand\labelitemiii{\textasteriskcentered}%
   \renewcommand\labelitemiv{\textasteriskcentered}%
   \begin{itemize}
}{%
   \end{itemize}}
%
\newenvironment{caselist}{%
   \def\textlistlabel{Case\ }%
   \begin{enumerate}
}{%
   \end{enumerate}
}
%
\newenvironment{steplist}{%
   \def\textlistlabel{Step\ }%
   \begin{enumerate}
}{%
   \end{enumerate}
}
%
\newenvironment{labellist}{%
   \begin{description}
}{%
   \end{description}
}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%% npara %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\NPARfont{}
\newcounter{ncount}
\newenvironment{npara}{\par%\addvspace{9pt plus2pt}%
   \NPARfont
   \setcounter{ncount}{0}%
   \def\item{\par\addtocounter{ncount}{1}\arabic{ncount}.\hskip2.6pt\ignorespaces}%
}{%
   \par}%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%% splist %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\fstparfont{\raggedright}
\newcounter{fstcount}
\newenvironment{fstpara}{\par\addvspace{11pt plus2pt}%
   \fstparfont
   \setcounter{fstcount}{0}%
   \def\item{\par\addtocounter{fstcount}{1}\arabic{fstcount})\hskip4.4pt\ignorespaces}%
}{%
   \par\addvspace{11pt plus2pt}\@endparenv}%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Macro 2: TheoremLike Env. %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\newif\ifTheorem
\global\Theoremfalse
%
\newcounter{theorem}
\renewcommand\thetheorem{\thechapter.\arabic{theorem}}
%
\newif\ifExample
\global\Examplefalse
%
\newif\ifrunon\runonfalse
%
\def\newtheorem#1{\@starthm{#1}\@ifnextchar[{\@othm{#1}}{\@nthm{#1}}}
\def\@starthm#1{\@namedef{#1*}{\@beginstarthm{#1}}%
	\@namedef{end#1*}{\@endstarthm{#1}}}
%
\def\@starthm#1{\@namedef{#1*}{\@beginstarthm{#1}}%
	\@namedef{end#1*}{\@endstarthm}}
%
\def\@beginstarthm#1{\@ifnextchar[{\@opargbeginstarthm{#1}}{\@opargbeginstarthm{#1}[]}}
%
\def\@opargbeginstarthm#1[#2]{\list{}{\topsep12pt plus2pt
 \def\@tempaa{#2}%
	\labelwidth0pt\labelsep9.5pt
	\leftmargin0pt
	\listparindent\parindent
 \edef\@Tempa{\csname #1name\endcsname}
	\def\makelabel##1{##1.}}
      \item[\hskip \labelsep{\csname#1headfont\endcsname \@Tempa{}\ifx\@tempaa\@empty\else\ (#2)\fi}]\csname#1font\endcsname}
%
\def\@endstarthm{\endlist}
%
\def\@xnthm#1#2[#3]{%
  \expandafter\@ifdefinable\csname #1\endcsname
    {\@definecounter{#1}\@newctr{#1}[#3]%
     \expandafter\xdef\csname the#1\endcsname{%
       \expandafter\noexpand\csname the#3\endcsname \@thmcountersep
          \@thmcounter{#1}}%
     \global\@namedef{#1}{\@thm{#1}{#2}{#1}}%
     \global\@namedef{end#1}{\@endtheorem}}}
\def\@ynthm#1#2{%
  \expandafter\@ifdefinable\csname #1\endcsname
    {\@definecounter{#1}%
     \expandafter\xdef\csname the#1\endcsname{\@thmcounter{#1}}%
     \global\@namedef{#1}{\@thm{#1}{#2}{#1}}%
     \global\@namedef{end#1}{\@endtheorem}}}
\def\@othm#1[#2]#3{%
  \@ifundefined{c@#2}{\@nocounterr{#2}}%
    {\expandafter\@ifdefinable\csname #1\endcsname
    {\global\@namedef{the#1}{\@nameuse{the#2}}%
  \global\@namedef{#1}{\@thm{#2}{#3}{#1}}%
  \global\@namedef{end#1}{\@endtheorem}}}}
\def\@thm#1#2#3{%
  \refstepcounter{#1}%
  \@ifnextchar[{\@ythm{#1}{#2}{#3}}{\@xthm{#1}{#2}{#3}}}
%
\def\@xthm#1#2#3{%
  \@opargbegintheorem{#2}{\csname the#1\endcsname}{}{#3}\ignorespaces}
\def\@ythm#1#2#3[#4]{%
  \@opargbegintheorem{#2}{\csname the#1\endcsname}{#4}{#3}\ignorespaces}
%
\def\@endtheorem{\par\addvspace{12pt plus2pt}\endlist}%
%
\def\@opargbegintheorem#1#2#3#4{\par\addvspace{12pt plus2pt}%
	\statementtype{#4}%
   \def\@tempa{#3}%
   \noindent{\csname #4headfont\endcsname\@ifundefined{xmlfile}{\ifx\@tempa\empty#1\ #2.\hskip9pt\else#1\ #2\ {\reset@font\itshape#3}.\hskip9pt\fi}{}}%
   \csname #4font\endcsname\ignorespaces}%
%
\def\statementtype#1{\gdef\@statementtype{#1}}
\def\@endtheorem{\ifthenelse{\equal{\@statementtype}{proof}}{\vskip-\baselineskip\hfill\QEDblogo}{}\par\addvspace{12pt plus2pt}}%
%
\def\examplename{Example}
\newtheorem{example}{\examplename}[chapter]
\def\theexample{\arabic{example}}
\def\examplefont{\itshape}
\def\exampleheadfont{\bfseries}
%
\def\theoremname{Theorem}
\newtheorem{theorem}{\theoremname}[section]
\def\thetheorem{\arabic{theorem}}
\def\theoremfont{\itshape}
\def\theoremheadfont{\bfseries}
%
\def\lemmaname{Lemma}
\newtheorem{lemma}{\lemmaname}[section]
\def\thelemma{\arabic{lemma}}
\def\lemmafont{\itshape}
\def\lemmaheadfont{\bfseries}
%
\def\propositionname{Proposition}
\newtheorem{proposition}{\propositionname}[section]
\def\theproposition{\arabic{proposition}}
\def\propositionfont{\itshape}
\def\propositionheadfont{\bfseries}
%
\def\corollaryname{Corollary}
\newtheorem{corollary}{\corollaryname}[section]
\def\thecorollary{\arabic{corollary}}
\def\corollaryfont{\itshape}
\def\corollaryheadfont{\bfseries}
%
\def\definitionname{Def{}inition}
\newtheorem{definition}{\definitionname}[section]
\def\thedefinition{\arabic{definition}}
\def\definitionfont{}
\def\definitionheadfont{\bfseries}
%
\def\notationname{Notation}
\newtheorem{notation}{\notationname}[section]
\def\thenotation{\arabic{notation}}%
\def\notationfont{\itshape}
\def\notationheadfont{\bfseries}
%
\def\assumptionname{Assumption}
\newtheorem{assumption}{\assumptionname}[section]
\def\theassumption{\arabic{assumption}}
\def\assumptionfont{\itshape}
\def\assumptionheadfont{\bfseries}
%
\def\remarkname{Remark}
\newtheorem{remark}{\remarkname}[section]
\def\theremark{\arabic{remark}}
\def\remarkfont{}
\def\remarkheadfont{\bfseries}
%
\def\proofname{Proof}
\newtheorem{proof}{\proofname}[section]
\def\theproof{\arabic{proof}}
\def\prooffont{}
\def\proofheadfont{}
%
\newif\ifQEDlogo
\QEDlogofalse
\font\QEDlogofont=msam10 at 9pt
\def\QEDlogo{%
        \ifQEDlogo
 	\else
	  \ifvmode
	    \vskip-\lastskip\hspace*{\fill}%
          \else
  	    \unskip\hskip5pt\ignorespaces
          \fi
          %\par
    	  \hfill{QED}%
          \global\QEDlogofalse
        \fi}
%
%%%%%% Proof %%%%%%
%
\def\prooffont{}
\font\QEDlogofont=msam10 at 10pt
\def\QEDlogo{\hbox{\QEDlogofont\char'003}}
\def\QEDblogo{\leavevmode{\QEDlogofont\char'004}}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  End TheoremLike Env. %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  comment %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\marginfont{\fontsize{9}{10}\selectfont\bfseries\raggedright}
\newcommand{\comment}[1]{%
 \setlength\overfullrule{0pt}%
 \ifodd\c@page
    \marginpar{%
    \parbox{8pc}{\par\vskip-1.5pt\marginfont please check.\par}}%
    \fboxsep.1pt\fbox{#1}%
 \else
    \marginpar{%
    \parbox{8pc}{\par\vskip-1.5pt\marginfont please check.\par}}
    \fboxsep.1pt\fbox{#1}\fi}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Floats %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\setcounter{topnumber}{5}
\renewcommand\topfraction{.9}
\setcounter{bottomnumber}{5}
\renewcommand\bottomfraction{.9}
\setcounter{totalnumber}{5}
\renewcommand\textfraction{.09}
\renewcommand\floatpagefraction{.901}
\setcounter{dbltopnumber}{5}
\renewcommand\dbltopfraction{.9}
\renewcommand\dblfloatpagefraction{.901}
%
\newlength\abovecaptionskip
\newlength\belowcaptionskip
\setlength\abovecaptionskip{9.5\p@}
\setlength\belowcaptionskip{4.25\p@}
%
\def\FigName{figure}
\def\BoxName{boxenv}
%
\long\def\@makecaption#1#2{%
    \ifx\FigName\@captype
      \vskip\abovecaptionskip
      \@makefigurecaption{#1}{#2}%
    \else
      \ifx\BoxName\@captype
        \@makeboxenvcaption{#1}{#2}%
        \vskip\belowcaptionskip
      \else%
        \@maketablecaption{#1}{#2}%
        \vskip\belowcaptionskip%
      \fi%
    \fi%
}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Figures %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\newif\ifFP
\global\FPfalse
\newif\ifCO
\global\COfalse
%
\newcounter{figure}[chapter]
\renewcommand\thefigure{\@arabic\c@figure}
\def\fps@figure{tbp}
\def\ftype@figure{1}
\def\ext@figure{lof}
\def\fnum@figure{\figurename\ \thefigure}
\newenvironment{figure}
               {\@float{figure}}
               {\end@float}
\newenvironment{figure*}
               {\@dblfloat{figure}}
               {\end@dblfloat}
%
\newenvironment{Figure}
               {\par\addvspace{12pt plus2pt}\def\@captype{figure}}
               {\par\addvspace{12pt plus2pt}}
%
\newenvironment{Figure*}
               {\par\addvspace{12pt plus2pt}\def\@captype{figure}}
               {\par\addvspace{12pt plus2pt}}
%
\newenvironment{sidefigure}
               {\let\@makefigurecaption\@makesidefigurecaption\@float{figure}}
               {\end@float}
%
\newenvironment{sidefigure*}
               {\let\@makefigurecaption\@makesidefigurecaption\@dblfloat{figure}}
               {\end@dblfloat}
%
\def\@makefigurecaption#1#2{\figcaptionfont%
\iffigcenter%
     \setbox\tempbox\hbox{\figcaptionfont{\figcaptionnumfont #1.}\unskip\enspace#2\par}%
     \ifdim\wd\tempbox >30pc%
        {\figcaptionfont{\figcaptionnumfont#1}.\unskip\enspace#2\vphantom{pqg}\par\vskip-2pt}%
     \else
        \centerline{\figcaptionfont{\figcaptionnumfont#1.}\unskip\enspace#2}%
  \fi
\else
        {\figcaptionfont{\figcaptionnumfont#1}.\unskip\enspace#2\vphantom{pqg}\par\vskip-2pt}%\hskip3.5pt
\fi
}
%
%
\def\@makesidefigurecaption#1#2{\fdimen\hsize%
     \advance\fdimen-\figwidth%
     \advance\fdimen-1pc%
     \setbox\tempbox\vbox to \figheight{\hsize\fdimen\vss{\figcaptionfont{\figcaptionnumfont #1}\unskip\enspace#2\par}\vss}%
     \ifdim\figwidth >14.75pc%
        \ifdim\figwidth <20pc%
            \vskip-\figheight%
                \centerline{\box\tempbox}%
      \else%
  \fi\fi%
  }
%
\def\ArtDir{art/}%
\input epsf.sty
%
\newbox\figtempbox
\def\ArtPiece#1{\epsfbox{\ArtDir#1}}%
%
\def\figurebox#1#2#3{%
    \@ifnextchar[{\@figurebox{#1}{#2}{#3}}{\@figurebox{#1}{#2}{#3}[]}}
%
\def\@figurebox#1#2#3[#4]{%
	  \def\temp{#1}%
	  \def\tempa{#2}%
	  \ifx\temp\@empty%
	  \else%
        \epsfysize#1%
	  \fi%
	  \ifx\tempa\@empty%
	  \else%
     	\epsfxsize#2%
	  \fi%
      \gdef\CO{CO}
      \gdef\FP{FP}
      \gdef\@thirdarg{#3}%
      \gdef\@frtharg{#4}%
      \ifx\@frtharg\empty
	  \ifx\temp\@empty%
         \global\figheight10pc
	  \else%
         \global\figheight#1
	  \fi%
	  \ifx\tempa\@empty%
         \global\figwidth10pc
	  \else%
         \global\figwidth#2
	  \fi%
         \ifx\@thirdarg\empty \FPfalse\COfalse\fi
      \else 
%%% for CO and FPO figure conditions
         \ifx\@thirdarg\empty \FPfalse\COfalse
         \else
           \ifx\@thirdarg\FP \FPtrue
           \else
             \ifx\@thirdarg\CO \COtrue
             \else
             \fi
           \fi
         \fi  
%%%
         \setbox\figtempbox=\hbox{\epsfbox{\ArtDir \ifCO #3-\else\ifFP#3-\fi\fi#4}}%
         \global\figwidth=\wd\figtempbox
         \global\figheight=\ht\figtempbox
       \fi
            \vbox to 0pt{\centerline{\figbox}}%%
%%% for marginal note
     \vskip-\baselineskip
     \ifodd\c@page
       \vtop to \figheight{\vfill\llap{\marginfont\ifFP 4-Color Artwork
                                                  \else\ifCO 4-Color Artwork
                                                  \else\fi\fi\hskip0.5pc}\vfill}%
     \else
       \vtop to \figheight{\vfill\llap{\marginfont\ifFP 4-Color Artwork
                                                  \else\ifCO 4-Color Artwork
                                                  \else\fi\fi\hskip0.5pc}\vfill}%
     \fi
%%%
}%
%%%%
\def\fpofigbox#1{\FPtrue\def\@fpo{#1}}
%
\def\whiteink{\special{color cmyk 0 0 0 0.0}}
\def\blackink{\special{color cmyk 0 0 0 1.0}}
%
\def\figbox{%
     \ifx\@frtharg\empty  
       \noindent\vbox{\hsize\figwidth%
	      \hrule\hbox to\figwidth{\vrule\hfill\vbox to\figheight{\hsize\figwidth\vfill}\vrule}\hrule}%
     \else
        \vbox{\vskip.8pt\hsize\figwidth
 	      \hbox to\figwidth{\vbox to\figheight{\hsize\figwidth\box\figtempbox}}}%
     \fi
     \ifCO\else\ifFP\vbox to 0pt{\vskip-.6\figheight\llap{\hbox to \figwidth{%
             \hfill\blackink\vrule height20pt width220pt depth5pt\whiteink
             \llap{\fontsize{26}{26}\selectfont\bfseries FPO scaled at \@fpo\%}\blackink\hfill}}}%
     \FPfalse\fi\fi%
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Tables %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\newcounter{table}[chapter]
\renewcommand\thetable{\@arabic\c@table}
\def\fps@table{tbp}
\def\ftype@table{2}
\def\ext@table{lot}
\def\fnum@table{\tablename\ \thetable}
\newenvironment{table}
               {\@float{table}}
               {\end@float}
\newenvironment{table*}
               {\@dblfloat{table}}
               {\end@dblfloat}
%
\newenvironment{Table}
               {\par\addvspace{12pt plus2pt}\def\@captype{table}}
               {\par\addvspace{12pt plus2pt}}
%
\newenvironment{Table*}
               {\par\addvspace{12pt plus2pt}\def\@captype{table}}
               {\par\addvspace{12pt plus2pt}}
%
\def\@maketablecaption#1#2{%
    {\tablecaptionfont\noindent{\tablecaptionnumfont#1}\unskip\enspace#2\vphantom{y}\par}}%\hskip3.5pt
%
\def\tbl#1#2{%
  \setbox\tempbox\hbox{\tablefont#2}%
  \tabledim\hsize
  \advance\tabledim-\wd\tempbox
  \ifdim\tabledim>0pt
    \divide\tabledim2
  \else
    \global\tabledim0pt
  \fi
  \global\tableleftskip\tabledim
  \global\tablerightskip\tabledim% plus1fill%
  \caption{#1}%
  {\centerline{\box\tempbox}}}%
%
\def\TCH#1{\TCHfont#1}%
%
\def\x{@{\extracolsep{\fill}}}
\def\toprule{\\[-8pt]\hline\\[-.5pt]}
\def\colrule{\\[-4.5pt]\hline\\[-0.3pt]}
\def\botrule{\\[1.5pt]\hline}
\def\crule#1{\\[-4.5pt]\cline{#1}\\[-0.3pt]}
%
\def\Hline{%
  \noalign{\ifnum0=`}\fi\hrule \@height 1.5pt \futurelet%\@height \arrayrulewidth
   \@tempa\@xhline}
%
\newenvironment{tabnote}{\par\addvspace{5pt}%
  \noindent\tabnotefont\ignorespaces%
  }{\par}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  End Floats %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Math %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\setlength\arraycolsep{1.5\p@}
\setlength\tabcolsep{6\p@}
\setlength\arrayrulewidth{.4\p@}
\setlength\doublerulesep{2\p@}
\setlength\tabbingsep{\labelsep}
\setlength\fboxsep{3\p@}
\setlength\fboxrule{.4\p@}
%
\setlength\columnsep{12\p@}
\setlength\columnseprule{0\p@}
%
\@addtoreset{equation}{chapter}
\renewcommand\theequation{\arabic{equation}}% 
\def\@eqnnum{{\reset@font\rmfamily(\theequation)}}
%
\def\tstrut{\vrule width0pt depth4.65pt}
\def\bstrut{\vrule width0pt height9pt}
\jot=3pt
%
\def\text#1{\mathchoice
  {\hbox{\fontsize{\tf@size}{\tf@size}\selectfont#1}}%
  {\hbox{\fontsize{\tf@size}{\tf@size}\selectfont#1}}%
  {\hbox{\fontsize{\sf@size}{\sf@size}\selectfont#1}}%
  {\hbox{\fontsize{\ssf@size}{\ssf@size}\selectfont#1}}}
%
% remove the following codes for centered equations
%%%%%%%%%%%%%%%%% normal mathindent
%
\mathindent12pt%
\AtEndOfClass{\mathindent\leftmargini}
\emathindent-12pt%
%
\newenvironment{equation*}{\relax
                \ifmmode\@badmath
                \else
                  \begin{trivlist}%
                    \@beginparpenalty\predisplaypenalty
                    \@endparpenalty\postdisplaypenalty
                    \item[]\leavevmode
                    \hb@xt@\linewidth\bgroup $\m@th\displaystyle %$
                      \hskip\mathindent\bgroup
                \fi}{\relax
                \ifmmode
                      \egroup $\hfil% 
                    \egroup
                  \end{trivlist}%
                \else \@badmath
                \fi}
%
\newenvironment{flequation}%
    {\@beginparpenalty\predisplaypenalty
     \@endparpenalty\postdisplaypenalty
     \refstepcounter{equation}%
     \trivlist \item[]\leavevmode
       \hb@xt@\linewidth\bgroup $\m@th% 
         \displaystyle
         \hskip\mathindent}%
        {$\hfil %
         \displaywidth\linewidth\hbox{\@eqnnum}%
       \egroup
     \endtrivlist}

%
\def\fleqnarray{\stepcounter{equation}%
\def\@currentlabel{\p@equation\theequation}%
\global\@eqnswtrue\m@th
\global\@eqcnt\z@\tabskip\mathindent
\let\\\@eqncr
$$\everycr{}\halign to\displaywidth\bgroup\hskip\@centering
  $\displaystyle\tabskip\z@skip{##}$\@eqnsel&\global\@eqcnt\@ne
  \hskip \tw@\arraycolsep \hfil${##}$\hfil
  &\global\@eqcnt\tw@ \hskip \tw@\arraycolsep
  $\displaystyle{##}$\hfil
   \tabskip\@centering&\global\@eqcnt\thr@@
       \hbox to\z@\bgroup\hss##\egroup\tabskip\z@skip\cr}
%
\def\endfleqnarray{%
      \@@eqncr
      \egroup
      \global\advance\c@equation\m@ne
   $$\@ignoretrue
}
%
\@namedef{fleqnarray*}{\def\@eqncr{\nonumber\@seqncr}\fleqnarray}
\@namedef{endfleqnarray*}{\nonumber\endfleqnarray}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  End Math %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Footnote %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\thanks#1{%\stepcounter{footnote}%
    \protected@xdef\@thanks{\@thanks
        \protect\footnotetext[\the\c@footnote]{#1}}%
}
%
%
\renewcommand\footnoterule{%
  \kern-3\p@
  \hrule width3pc height.5pt%\columnwidth%
  \kern 2.7\p@}
%
\@addtoreset{footnote}{chapter}
\renewcommand\thefootnote{\arabic{footnote}}
%
\def\@fnsymbol#1{\ifcase#1\or *\or \dagger\or \ddagger\or
   \SS\or \|\or \#\or **\or \dagger\dagger\or \ddagger\ddagger 
   \or \SS\SS \or \|\hskip-1pt\|\or \#\#\or ***\or 
   \dagger\dagger\dagger\or \ddagger\ddagger\ddagger\else\@ctrerr\fi\relax}
%
\newdimen\@footmax
\def\footmax#1{%
  \setbox\tempbox\hbox{\footnotesize$^{#1}$\hskip.5em}%
  \global\@footmax\wd\tempbox}
%
\footmax{1}
%
\long\def\@makefntext#1{\let\doPar\relax%
    \noindent{{\@makefnmark\hskip.5em}}#1% \hskip.5em
}
%
\def\corresinfo#1{%
  \def\@makefnmark{}%\hbox{\@textsuperscript{\normalfont\@thefnmark}}}%
  \footnotetext{\hspace*{-0pt}#1}
  \def\@makefnmark{\hbox{\@textsuperscript{\normalfont\@thefnmark}}}%
}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  End Footnote %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Page styles  %%%%%%%%%%%%%%%%%%%%%%%%%%%
%%
\def\copyeditor#1{\gdef\@copyeditor{#1}}\copyeditor{}
\def\jvol#1{\gdef\@jvol{#1}}
\def\jnum#1{\gdef\@jnum{#1}}
\def\jslugname#1{\jslugnamefalse\gdef\@jslugname{#1}}
\def\jmonth#1{\gdef\@jmonth{#1}}
\def\jyear#1{\gdef\@jyear{#1}}
\def\jend#1{\gdef\@jend{#1}}
\def\issn#1{\gdef\@issn{#1}}

\def\jname#1{\gdef\@jname{#1}%
             \gdef\@jtitle{\uppercase{#1}}}
\def\@jtitle{}

\def\jdate#1{\gdef\@jdate{#1}}
\def\endpage#1{\gdef\l@page{#1}}%\gdef\@endpage{#1}}
\def\doi#1{\gdef\@doi{#1}}
\def\pubid#1{\gdef\@pubid{#1}}
\def\@pubid{}%

\def\fpage#1{\setcounter{page}{#1}\gdef\f@page{#1}}%
\def\lpage#1{\gdef\l@page{#1}}%

\def\cpyyear#1{\gdef\@cpyyear{#1}}%

\def\accessdate#1{\gdef\@accessdate{#1}}
\def\footinfo#1{\gdef\@footinfo{#1}}
\def\copyrightinfo#1{\gdef\@cpyinfo{\Copyright\ #1}}
%
\def\@doi{}
\def\@jvol{}
\def\@jnum{}
\def\@jyear{}
\def\@jslugname{}%
\def\@jmonth{}
\def\@jyear{}
\def\@jend{99}
\def\@issn{}
\def\@jname{}
\def\f@page{}%
\def\l@page{}%
\def\@cpyyear{}%
\def\@endpage{}%
\def\@accessdate{}%
\def\@footinfo{}%
\def\@cpyinfo{}%
%
\def\oddfolio{{\foliofont\thepage}}
\def\evenfolio{{\foliofont\thepage}}
%
\def\ps@headings{%
    \def\@evenhead{\evenfolio\hfill{\rhfont\leftmark}}%
    \def\@oddhead{{\rhfont\rightmark}\hfill\oddfolio}%
    \let\@oddfoot\@empty\let\@evenfoot\@empty
    \let\@mkboth\markboth
    \def\chaptermark##1{\markboth{##1}{##1}}%
}
%
\def\ps@empty{%
      \def\@oddfoot{}%
      \let\@evenfoot\@oddfoot
      \def\@evenhead{}%
      \def\@oddhead{}%
      \let\@mkboth\markboth
      \let\chaptermark\@gobble
      \let\sectionmark\@gobble}
%
\def\Copyright{\leavevmode\raise.2ex\hbox{\fontsize{7}{7}\selectfont{\ooalign{\hfil\raise0ex\hbox{\kern-.3pt\fontsize{5}{7}\selectfont C}%
                \hfil\crcr \mathhexbox20D}}}}
%
\def\plain@page{no}%
\def\ps@plain{\let\@mkboth\@gobbletwo\gdef\plain@page{yes}%
	\fpage{\thepage}%
       \def\@evenhead{{\RHfont%
         \vbox{\hsize\textwidth%
           \hbox{{\RHfont%
                 \ifx\@jname\@empty\else\@jname\fi%
                 \ifx\@jyear\@empty\else\unskip\ (\@jyear)\fi%
                      \ifx\@jvol\@empty\else\ \@jvol\unskip{:}\fi%
                 \ifx\f@page\@empty\else\ \f@page\fi%
                 \ifx\l@page\@empty\else--\l@page\fi%
           }}\par%
           \hbox{\RHfont\ifx\@doi\@empty\else{doi:}\ \@doi\fi}\par%
           \hbox{{\RHfont\ifx\@accessdate\@empty\else\@accessdate\fi}}\fi%
          }}}%
       \def\@oddhead{{\RHfont%
         \vbox{\hsize\textwidth%
           \hbox{{\RHfont%
                 \ifx\@jname\@empty\else\@jname\fi%
                 \ifx\@jyear\@empty\else\unskip\ (\@jyear)\fi%
                        \ifx\@jvol\@empty\else\ \@jvol\unskip{:}\fi%
                 \ifx\f@page\@empty\else\ \f@page\fi%
                 \ifx\l@page\@empty\else--\l@page\fi%
           }}\par%
           \hbox{{\RHfont\ifx\@doi\@empty\else{doi:}\ \@doi\fi}}\par%
           \hbox{{\RHfont\ifx\@accessdate\@empty\else\@accessdate\fi}}%
          }}}%
      \def\@evenfoot{\raise3pt\vbox{\vskip\baselineskip{\cpyinfofont%
                       {\ifx\@cpyinfo\@empty\else{\cpyinfofont\@cpyinfo}\fi}\par%
                      }}}%
       \def\@oddfoot{\raise3pt\vbox{\vskip\baselineskip{\cpyinfofont%
                       {\ifx\@cpyinfo\@empty\else{\cpyinfofont\@cpyinfo}\fi}\par%
                      }}}%
}
%
\def\receivedfont{\fontsize{8}{9}\selectfont\itshape}
\def\printdates{\par\vskip2.5pt%
   \ifx\@received\@empty\else\noindent{\receivedfont{Received for publication:}\ \@received\par}\fi\gdef\@received{}%
   \ifx\@accepted\@empty\else\noindent{\receivedfont{Accepted in revised form:}\ \@accepted\par}\fi\gdef\@accepted{}%
}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  End Page styles  %%%%%%%%%%%%%%%%%%%%%%%%
%
\newenvironment{thebibliography}{}{}
\usepackage[authoryear]{natbib}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Bibliography Section   %%%%%%%%%%%%%%%%%%
%
\newdimen\bibindent
\newdimen\bibleftmargin
\newdimen\bibitemsep
\newdimen\bibparsep
\newdimen\bibtext
\newdimen\biblabelsep
\newdimen\bibleftmargini
%
%%%%% TRUE FOR CHAPTER TITLE AND FALSE FOR SECTION TITLE %%%%%%%%
\newif\ifbibchapter
\global\bibchaptertrue
%%%%%%%% Unnumberd References %%%%%%%%%%%
\setlength\bibleftmargin  {10pt}
\setlength\bibitemsep  {0pt}
\setlength\bibparsep  {0pt}
%%%%%%%% Numbered Within Squre Bracket %%%%%%%%%%%
\newif\ifnumsqure
\setlength\biblabelsep  {3.5pt}
\setlength\bibleftmargini  {3.75pt}
%%%%%%%% Numbered With Dot %%%%%%%%%%%%%%%
\setlength\bibtext  {12pt}
\def\@biblabel#1{#1}
%
\renewenvironment{thebibliography}[1]{\overfullrule0pt%
\addvspace{20pt}%
 \section*{\bibname}%
  \bibliofont%
     \def\@tempa{#1}%
     \ifx\@tempa\@empty
         \list{}%
           {\labelwidth0pt\labelsep0pt
           \leftmargin\z@%\bibleftmargin%12
           \itemsep\bibitemsep
           \parsep\bibparsep
           \usecounter{enumiv}%
           \let\p@enumiv\@empty
           \renewcommand\theenumiv{\arabic{enumiv}}}%
      \else
          \setbox\tempbox\hbox{\@tempa}% \@tempa.
          \tempdimen\wd\tempbox
          \ifnumsqure
          \else
          \def\@biblabel##1{{\hbox to \tempdimen{\hfill##1}}}\fi%
           \list{\@biblabel{\arabic{enumiv}}}%
           {\settowidth\labelwidth{\@biblabel{#1}}%
           \labelsep\biblabelsep\leftmargin\labelsep
               \advance\leftmargin\labelwidth
           \itemindent0pt
           \itemsep\bibitemsep
           \parsep\bibparsep
           \usecounter{enumiv}%
           \let\p@enumiv\@empty
           \renewcommand\theenumiv{\arabic{enumiv}}}%
     \fi
     \sloppy\clubpenalty4000\widowpenalty4000%
     \sfcode`\.=\@m}
     {\def\@noitemerr
     {\@latex@warning{Empty `thebibliography' environment}}%
     \endlist%
     \reset@font}
\newcommand\newblock{}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  End Bibliography Section %%%%%%%%%%%%%%%%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% FM  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\newcommand\@pnumwidth{1.55em}
\newcommand\@tocrmarg {2.55em}
\newcommand\@dotsep{4.5}
\setcounter{tocdepth}{2}
%
\newcommand\l@part[2]{%
  \ifnum \c@tocdepth >-2\relax
    \addpenalty{-\@highpenalty}%
    \addvspace{2.25em \@plus\p@}%
    \begingroup
      \setlength\@tempdima{3em}%
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      {\leavevmode
       \large \bfseries #1\hfil \hbox to\@pnumwidth{\hss #2}}\par
       \nobreak
         \global\@nobreaktrue
         \everypar{\global\@nobreakfalse\everypar{}}
    \endgroup
  \fi}
\newcommand\l@chapter[2]{%
  \ifnum \c@tocdepth >\m@ne
    \addpenalty{-\@highpenalty}%
    \vskip 1.0em \@plus\p@
    \setlength\@tempdima{1.5em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode \bfseries
      \advance\leftskip\@tempdima
      \hskip -\leftskip
      #1\nobreak\hfil \nobreak\hbox to\@pnumwidth{\hss #2}\par
      \penalty\@highpenalty
    \endgroup
  \fi}
\newcommand\l@section      {\@dottedtocline{1}{1.5em}{2.3em}}
\newcommand\l@subsection   {\@dottedtocline{2}{3.8em}{3.2em}}
\newcommand\l@subsubsection{\@dottedtocline{3}{7.0em}{4.1em}}
\newcommand\l@paragraph    {\@dottedtocline{4}{10em}{5em}}
\newcommand\l@subparagraph {\@dottedtocline{5}{12em}{6em}}
\let\l@table\l@figure
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  End FM  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  DefList  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\newcount\deflistcount

\def\deflistmax#1#2{\expandafter\xdef\csname deflistmax@\romannumeral#1\endcsname{#2}}%

\newenvironment{deflist}{\par\addvspace{12pt}%
  \global\advance\deflistcount\@ne%
  \@ifundefined{deflistmax@\romannumeral\deflistcount}{\expandafter\xdef\csname deflistmax@\romannumeral\deflistcount\endcsname{0pt}}{}%
  \noindent\ignorespaces%
  }{\par\addvspace{12pt}%
  \immediate\write\@mainaux{\string\deflistmax{\the\deflistcount}{\csname deflistmax@\romannumeral\deflistcount\endcsname}}%
  }
\def\YES{yes}
\def\deflistentry#1#2{%
  \setbox\@tempboxa\hbox{\ifx\withinappendix\YES\appendixfont\fi#1\hspace*{9.5pt}}%
  \@tempdima\wd\@tempboxa%
  \expandafter\ifdim\@tempdima>\csname deflistmax@\romannumeral\deflistcount\endcsname%
    \expandafter\xdef\csname deflistmax@\romannumeral\deflistcount\endcsname{\the\@tempdima}%
  \else%
    \global\@tempdima\csname deflistmax@\romannumeral\deflistcount\endcsname\relax%
  \fi%
  \noindent\hbox to \@tempdima{\ifx\withinappendix\YES\appendixfont\fi#1\hfill}\unskip{\hangindent\@tempdima#2\par}%
}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Appendix  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\newcommand\appendix{\par
  \setcounter{chapter}{0}%
  \setcounter{section}{0}%
  \renewcommand\thechapter{\Alph{chapter}}
  \renewcommand\theequation{A\arabic{equation}}
  \setcounter{equation}{0}%
}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% End Appendix %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  Index  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\alphabet#1{{\bf#1}\par\vskip.5\baselineskip}
%
\newenvironment{theindex}{\thispagestyle{plain}%
      \columnseprule \z@
      \columnsep 12\p@
      \indexfont\markboth{\indexname}{\indexname}
      \tempdimen\normalbaselineskip
      \advance\tempdimen-\baselineskip
      \twocolumn[\@makeschapterhead{\indexname}\vskip\tempdimen]%
      \parindent\z@
      \let\item\@idxitem
}{%
      \par}
\newcommand\@idxitem  {\par\hangindent3em}
\newcommand\subitem   {\par\hangindent3em\hspace*{1em}}
\newcommand\subsubitem{\par\hangindent3em\hspace*{2em}}
\newcommand\indexspace{\par \vskip\baselineskip}
%
%%%%%%%%%%%%%%%%%%%% File Version  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%
\def\document{\endgroup
  \ifx\@unusedoptionlist\@empty\else
    \@latex@warning@no@line{Unused global option(s):^^J%
            \@spaces[\@unusedoptionlist]}%
  \fi
  \@colht\textheight
  \@colroom\textheight \vsize\textheight
  \columnwidth\textwidth
  \@clubpenalty\clubpenalty
  \if@twocolumn
    \advance\columnwidth -\columnsep
    \divide\columnwidth\tw@ \hsize\columnwidth \@firstcolumntrue
  \fi
  \hsize\columnwidth \linewidth\hsize
  \begingroup\@floatplacement\@dblfloatplacement
    \makeatletter\let\@writefile\@gobbletwo
    \global \let \@multiplelabels \relax
    \@input{\jobname.aux}%
  \endgroup
  \if@filesw
    \immediate\openout\@mainaux\jobname.aux
    \immediate\write\@mainaux{\relax}%
  \fi
  \process@table
  \let\glb@currsize\@empty  %% 
  \normalsize
  \everypar{}%
  \@noskipsecfalse
  \let \@refundefined \relax
  \let\AtBeginDocument\@firstofone
  \@begindocumenthook
  \ifdim\topskip<1sp\global\topskip 1sp\relax\fi
  \global\@maxdepth\maxdepth
  \global\let\@begindocumenthook\@undefined
  \ifx\@listfiles\@undefined
    \global\let\@filelist\relax
    \global\let\@addtofilelist\@gobble
  \fi
  \gdef\do##1{\global\let ##1\@notprerr}%
  \@preamblecmds
  \global\let \@nodocument \relax
  \ignorespaces}
%
  \def\draftnote{}
  \def\comment{}
  \def\Qauthor#1{}
   \def\QtoAuthor#1{}
   \def\QtoClient#1{}
   \def\QtoQC#1{}
   \def\QtoGL#1{}
   \def\qtoa#1{}
\let\qtoa\Qauthor
%
%%%%%%%%%%%%%%%%%%%% Character count  %%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\gray{\special{color CMYK 0 0 0 0.5}}
\def\@questionmark{\vbox to 0pt{\vskip13pc\hskip-5pc
                  \hbox to \textwidth{\special{color push CMYK 0 0 0 0.5}\fontsize{570}{570}\selectfont ?
                  \special{color pop}\hss}}}
\def\questionmark#1{\xdef\@questionmark{#1}}%
%
\def\@TotalChars{}
\def\TotalChars#1{\xdef\@TotalChars{#1}}%
%%
%
\def\enddocument{%
   \@enddocumenthook
   \@checkend{document}%
       \immediate\write\@mainaux{\string\endpage{\thepage}}%
   \clearpage
   \begingroup
     \if@filesw
       \immediate\write\@mainaux{\string\questionmark{}}%
       \immediate\closeout\@mainaux
       \let\@setckpt\@gobbletwo
       \let\@newl@bel\@testdef
       \@tempswafalse
       \makeatletter \input\jobname.aux
     \fi
     \@dofilelist
     \ifdim \font@submax >\fontsubfuzz\relax
       \@font@warning{Size substitutions with differences\MessageBreak
                  up to \font@submax\space have occured.\@gobbletwo}%
     \fi
     \@defaultsubs
     \@refundefined
     \if@filesw
       \ifx \@multiplelabels \relax
         \if@tempswa
           \@latex@warning@no@line{Label(s) may have changed.
               Rerun to get cross-references right}%
         \fi
       \else
         \@multiplelabels
       \fi
     \fi
   \endgroup
   \deadcycles\z@\@@end}
%
%%%%%%%%%%%%%%%%%%%%%%%  %%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\newdimen\tempdim
\newdimen\presentfigwidth
\newdimen\oldfigwidth
\newdimen\remainingtextwidth
%
\def\cropmarks{\nointerlineskip\vbox to 0pt{\offinterlineskip\vss
  \hbox to \trimwidth{\vbox to 0pt{\draftnote}\hfill}}}%

\def\croprules{%
		\nointerlineskip\vbox to 0pt{\offinterlineskip
  \vskip4pt\cropmarks
		\vskip\topmargin
  \hbox to \trimwidth{\hskip\@themargin\hbox to \textwidth{\hss%
      \vrule height0pt depth\typeheight width.1pt%
      \vrule height.1pt depth0pt width\textwidth
      \vrule height0pt depth\typeheight width.1pt\hss}}%
  \hbox to \trimwidth{\hskip\@themargin\hbox to \textwidth{\hss%
      \vrule height.1pt depth0pt width\textwidth\hss}\hss}
}}
%
%
\figwidth0pt
\figheight0pt
%
%%%%%%%%%%%%%%%%%%% End File Version %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Trimmarks  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\def\trimmarks{%
  \vbox to 0pt{%
     \vskip-25pt\parindent0pt
     \draftnote\offinterlineskip}%
  \ifdraft
    \vbox to 0pt{\hsize\trimwidth\offinterlineskip
    \parindent0pt\leftskip0pt\rightskip0pt
    \fboxsep0pt\fboxrule\draftrule
    \fbox{\vbox{\vskip\trimheight\hskip\trimwidth}}}%
%
    \vbox to 0pt{\hsize\trimwidth\offinterlineskip
    \parindent0pt\leftskip0pt\rightskip0pt
    \vbox to \trimheight{\offinterlineskip\parindent0pt
    \hbox to \trimwidth{\vbox to 2pc{\vskip-3.5pc\hbox{\vrule height2pc width\trimrule}}\raisebox{2pc}{\hbox{\hskip-3.5pc\vrule width2pc height\trimrule}}\hfill
      \raisebox{2pc}{\vrule width2pc height\trimrule\hskip-3.75pc}
      \vbox to 2pc{\vskip-3.5pc\hbox{\vrule height2pc width\trimrule}}%
    }\vfill
    \hbox to \trimwidth{\hbox{\hskip-3.5pc\vrule height\trimrule width2pc}\vbox to 3pc{\vspace*{4.5pc}\hbox{\hskip1.5pc\vrule width\trimrule height2pc}}\hfill
    \vbox to 3.5pc{\vskip5pc\hbox{\vrule height2pc width\trimrule}}\rlap{\hskip1.5pc\vrule width2pc height\trimrule}}}}%
%    
  \else
    \vbox to 0pt{\hsize\trimwidth\offinterlineskip
    \parindent0pt\leftskip0pt\rightskip0pt
    \vbox to \trimheight{\offinterlineskip\parindent0pt
    \hbox to \trimwidth{\vbox to 2pc{\vskip-3.5pc\hbox{\vrule height2pc width\trimrule}}\raisebox{2pc}{\hbox{\hskip-3.5pc\vrule width2pc height\trimrule}}\hfill
      \raisebox{2pc}{\vrule width2pc height\trimrule\hskip-3.75pc}
      \vbox to 2pc{\vskip-3.5pc\hbox{\vrule height2pc width\trimrule}}%
    }\vfill
    \hbox to \trimwidth{\hbox{\hskip-3.5pc\vrule height\trimrule width2pc}\vbox to 3pc{\vspace*{4.5pc}\hbox{\hskip1.5pc\vrule width\trimrule height2pc}}\hfill
    \vbox to 3.5pc{\vskip5pc\hbox{\vrule height2pc width\trimrule}}\rlap{\hskip1.5pc\vrule width2pc height\trimrule}}}}
\fi
\insidedraftrules}
%
\def\insidedraftrules{\vbox to 0pt{%
  \offinterlineskip\parindent0pt
  \vskip \topmargin
  \tempdimen\normaltextheight
  \advance\tempdimen\headheight
  \advance\tempdimen\headsep
  \moveright\@themargin
  \vbox{\vbox to 0pt{\vskip\headheight\vskip\headsep
   \vrule height\draftrule width\textwidth}
   \hbox{\fboxsep0pt\fboxrule\draftrule
        \fbox{\vbox to \tempdimen
                    {\hsize\textwidth\hskip\textwidth}}}}}}%
%
\def\insidedraftrules{%
\vbox to 0pt{%
  \offinterlineskip\parindent0pt
  \vskip \topmargin
  \tempdimen\normaltextheight
  \advance\tempdimen\headheight
  \advance\tempdimen\headsep
  \advance\tempdimen-0.4pt
  \moveright\@themargin
      \ifodd\c@page
         \hbox to \textwidth{\hss\hbox to \typewidth{%
         \vbox to \tempdimen{\hrule height\draftrule
         \vbox to 0pt{\vskip\headheight\vskip\headsep%\vskip-6pt
                \hbox{\vrule height\draftrule width\typewidth}}%
         \hbox to \typewidth{\vrule width\draftrule\hskip\columnwidth\vrule width\draftrule\hskip\columnsep\vrule width\draftrule%
         \hfill\vrule height\tempdimen width\draftrule}%
         \hrule height\draftrule}}}%
      \else%
         \hbox to \textwidth{\hss\hbox to \typewidth{%
         \vbox to \tempdimen{\hrule height\draftrule
         \vbox to 0pt{\vskip\headheight\vskip\headsep%
                \hbox{\vrule height\draftrule width\typewidth}}%
         \hbox to \typewidth{\vrule width\draftrule\hskip\columnwidth\vrule width\draftrule\hskip\columnsep\vrule width\draftrule%
         \hfill\vrule height\tempdimen width\draftrule}%
         \hrule height\draftrule}}}%
      \fi}}%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%%%%%%%%%%%%%%%%%
\def\insidedraftrules{%
\vbox to 0pt{\ifnum\thepage=0\else\fi%
  \offinterlineskip\parindent0pt
  \vskip \topmargin
  \tempdimen\normaltextheight
  \advance\tempdimen\headheight
  \advance\tempdimen\headsep
  \advance\tempdimen-0.4pt
  \moveright\@themargin
      \ifodd\c@page
         \hbox to \textwidth{\hss\hbox to \typewidth{%
         \vbox to \tempdimen{\hrule height\draftrule
         \vbox to 0pt{\vskip\headheight\vskip\headsep%\vskip-6pt
                \hbox{\vrule height\draftrule width\typewidth}}%
         \hbox to \typewidth{\vrule width\draftrule
         \hfill\vrule height\tempdimen width\draftrule}%
         \hrule height\draftrule}}}
      \else%
         \hbox to \textwidth{\hss\hbox to \typewidth{%
         \vbox to \tempdimen{\hrule height\draftrule
         \vbox to 0pt{\vskip\headheight\vskip\headsep%\vskip-6pt
                \hbox{\vrule height\draftrule width\typewidth}}%
         \hbox to \typewidth{\vrule width\draftrule
         \hfill\vrule height\tempdimen width\draftrule}%
         \hrule height\draftrule}}}
      \fi}}%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% End Trimmarks  %%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Output Routine  %%%%%%%%%%%%%%%%%%%%%%%%%%
%%
\def\@outputpage{%
\begingroup           % the \endgroup is put in by \aftergroup
  \let \protect \noexpand
  \@resetactivechars
  \@parboxrestore
  \shipout \vbox{%
    \set@typeset@protect
    \aftergroup \endgroup
    \aftergroup \set@typeset@protect
  \if@specialpage
    \global\@specialpagefalse\@nameuse{ps@\@specialstyle}%
  \fi
  \if@twoside
    \ifodd\count\z@ \let\@thehead\@oddhead \let\@thefoot\@oddfoot
         \let\@themargin\oddsidemargin
    \else \let\@thehead\@evenhead
       \let\@thefoot\@evenfoot \let\@themargin\evensidemargin
    \fi
  \fi
  \reset@font
  \normalsize
  \baselineskip\z@skip \lineskip\z@skip \lineskiplimit\z@
    \@begindvi\trimmarks
    \vskip \topmargin
    \moveright\@themargin \vbox {%
      \setbox\@tempboxa \vbox to\headheight{%
        \vfil
        \color@hbox
          \normalcolor
          \hb@xt@\textwidth {%
            \let \label \@gobble
            \let \index \@gobble
            \let \glossary \@gobble %%
            \@thehead
            }%
        \color@endbox
        }%                        %%
      \dp\@tempboxa \z@
      \box\@tempboxa
      \vskip \headsep
      \box\@outputbox
      \baselineskip \footskip
      \color@hbox
        \normalcolor
        \hb@xt@\textwidth{%
          \let \label \@gobble
          \let \index \@gobble      %%
          \let \glossary \@gobble   %%
          \@thefoot
          }%
      \color@endbox
      }%
    }%
\global \@colht \textheight
\stepcounter{page}%
\gdef\plain@page{no}%
\let\firstmark\botmark
  \ifodd\c@page
     \ifspreadlong\global\spreadlongfalse
     \enlargethispage{\@spreadlong}\fi
  \fi
}
%
%%%%%%%%%%%%%%%%%%%%%%%% Misc. %%%%%%%%%%%%%%%%%%%%%%%
%
\def\@@question#1{\hbox to \hsize{\hfill
                   \rlap{\hskip\marginparsep
                         \vbox to 0pt{\hsize\marginparwidth
                                      \footnotesize
                                      \raggedright#1\endgraf\vss}}}}
\def\@question#1{\ifvmode
                    \@@question{#1}%
                 \else
                     \vadjust{\vbox to 0pt{%
                     \vskip-7.5pt\@@question{#1}\vskip7.5pt}}
                 \fi
}
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% End Output Routine  %%%%%%%%%%%%%%%%%%%%%%
%
\newif\ifspreadlong
\def\spreadlong#1{\ifodd\c@page\wlog{Ignoring spreadlong}
                  \else
                     \spreadlongtrue\gdef\@spreadlong{#1}%
                     \enlargethispage{#1}%
                  \fi}
% check specs and enable one or both of these commands
\def\leaflong#1{\enlargethispage{#1}}
%
%%%%%%%%%%%%%%%%%%%%%%%%% Initialization  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\usepackage[figuresleft]{rotating}
%
\medmuskip=4mu 
\thickmuskip=5mu 
%
\pagestyle{headings}
\pagenumbering{arabic}      % Arabic page numbers
\sloppy
\frenchspacing
\voffset-74pt
\hoffset-74pt
\marginparsep2.5pc
%
%============================================
\newcount\authorcount
\newcount\affcount
\newcount\tempcount
\def\pound{\hbox{\char'243}}
\def\rffont{\fontsize{8}{9}\selectfont}
%
%=========================================================
\let\copyright\Copyright
\endinput
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% End Initialization %%%%%%%%%%%%%%%%%%%%%%%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Extras %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% End Extras %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
