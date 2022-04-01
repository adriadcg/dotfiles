" --------------------------------
"  PLUGINS
"  ------------------------------

call plug#begin('~/.config/nvim/plugged') 
" ============= PLUGS START ===================

" ============================================= 
"                  IDE
" ============================================= 
Plug 'junegunn/fzf'
Plug 'junegunn/fzf.vim'
Plug 'mhinz/vim-signify'
Plug 'yggdroot/identline'
Plug 'scrooloose/nerdcommenter'

" Highlight UI elements based on current mode
" https://github.com/mvllow/modes.nvim
Plug 'vllow/modes.nvim'

" ============================================= 
"                  Markdown
" ============================================= 
Plug 'godlygeek/tabular'
" Markdown (https://github.com/preservim/vim-markdown)
Plug 'preservim/vim-markdown'
Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app && yarn install'  }
" Git (https://github.com/tpope/vim-fugitive) 
Plug 'tpope/vim-fugitive'

"" Move searching 2 characteres
Plug 'easymotion/vim-easymotion'
" Show html colors
Plug 'chrisbra/Colorizer'
" Syntaxis Highlight
Plug 'sheerun/vim-polyglot'

Plug 'junegunn/limelight.vim'
" Statusbar
Plug 'nvim-lualine/lualine.nvim'
Plug 'kyazdani42/nvim-web-devicons' " Recommended (for coloured icons)
Plug 'ryanoasis/vim-devicons' "Icons without colours

" ============================================= 
"                  Themes
" ============================================= 
Plug 'sonph/onehalf', { 'rtp': 'vim' }
Plug 'catppuccin/nvim', {'as': 'catppuccin'}
Plug 'EdenEast/nightfox.nvim'


" Typing
Plug 'jiangmiao/auto-pairs'
Plug 'alvan/vim-closetag'
Plug 'tpope/vim-surround'
" Autocomplete
Plug 'sirver/ultisnips'
Plug 'neoclide/coc.nvim', {'branch':'release'}
" Unicode
Plug 'chrisbra/unicode.vim'
" Test
Plug 'tyewang/vimux-jest-test'
Plug 'janko-m/vim-test'


" ============================================= 
"            Working with buffers
" ============================================= 
" Buffers in tabs
" Plug 'akinsho/bufferline.nvim'
"" Tree file view
" Plug 'kyazdani42/nvim-tree.lua'

Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'

" =============PLUGS END =====================
call plug#end()
