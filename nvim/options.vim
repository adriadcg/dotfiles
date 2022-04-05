set nocompatible
" GUI config
set number " Show row's numbers 
set numberwidth=2
set title " Show the file name in the terminal's window
set mouse=a " Enable mouse integration (Select text, move cursor)
syntax on
set showcmd
set ruler
set encoding=utf-8
set showmatch
set relativenumber
set laststatus=2
set t_Co=256
set guifont=FiraCore\ Nerd\ Font\10

set termguicolors " Activate true colors on terminal
" set background=dark " Background color
" Theme config
colorscheme onehalfdark
" nightfox 
" let g:airline_theme='onehalfdark'
" let g:lightline = { 'colorscheme': 'onehalfdark' }

" Internal visualization config
set nowrap  " Disable line separation
set cursorcolumn " Highlight actual column
set cursorline " Highlight actual line

set colorcolumn=120 " Show column with 120 characters limit

" Identation to 4 spaces
set tabstop=4
set shiftwidth=4
set softtabstop=4
set shiftround
set expandtab " Insert spaces in change of tabs
set sw=2

" Function's config
set hidden " Enable buffer change without save before

" FILE BROWSING:
" Tweaks for browsing
let g:netrw_keepdit=0
let g:netrw_winsize=25
let g:netrw_fastbrowse=0
let g:netrw_banner=0        " disable annoying banner
let g:netrw_browse_split=4  " open in prior window
let g:netrw_altv=1          " open splits to the right
let g:netrw_liststyle=3     " tree view
let g:netrw_list_hide=netrw_gitignore#Hide()
let g:netrw_list_hide.=',\(^\|\s\s\)\zs\.\S\+'

" Search's config
" Search down into subfolders
set path+=** " Provides tab-completion for all file-related tasks
set wildmenu " Display all matchin files when we tab complete

" Create the `tags` file (may need to install ctags first)
" Inspired by https://www.youtube.com/watch?v=XA2WjJbmmoM&t=907s
command! MakeTags !ctags -R

set ignorecase " Searches are case insensitive
set smartcase " Not ignore mayus if searched word contains at least one capital letter
set hlsearch " Highlight matches
set incsearch " Incremental searching

" Dictionary's config
set spelllang=en,es " Correct words using english and spanish's dictionaries
