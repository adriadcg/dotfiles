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
" Signify uses the sign column to indicate added, modified and removed
" lines in a file that is managed by a version control system (VCS)
" https://github.com/mhinz/vim-signify
Plug 'mhinz/vim-signify'
Plug 'Yggdroot/indentLine'
Plug 'scrooloose/nerdcommenter'
Plug 'neovim/nvim-lspconfig'
Plug 'ray-x/lsp_signature.nvim'

" Treesitter configurations and abstraction layer for Neovim.
" https://github.com/nvim-treesitter/nvim-treesitter
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
" Highlight UI elements based on current mode
" https://github.com/mvllow/modes.nvim
Plug 'mvllow/modes.nvim'
Plug 'kyazdani42/nvim-tree.lua'

" Syntax highlighting for Kitty terminal config files.
" Any *.conf or *.session files in kitty's configuration directory is considered.
" You can always add # vim:ft=kitty at the beginning of any file to make sure the syntax is loaded,
" or you can set it temporarily with :set ft=kitty.
" https://github.com/fladson/vim-kitty
Plug 'fladson/vim-kitty'

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
" Hyperfocus-writing in Vim.
" https://github.com/junegunn/limelight.vim
Plug 'junegunn/limelight.vim'
" Statusbar
Plug 'nvim-lualine/lualine.nvim'
Plug 'kyazdani42/nvim-web-devicons' " Recommended (for coloured icons)
Plug 'ryanoasis/vim-devicons' "Icons without colours
Plug 'rhysd/vim-grammarous'
" ============================================= 
"                  Themes
" ============================================= 
Plug 'sonph/onehalf', { 'rtp': 'vim' }
Plug 'catppuccin/nvim', {'as': 'catppuccin'}
Plug 'EdenEast/nightfox.nvim'
Plug 'folke/tokyonight.nvim', { 'branch': 'main' }
" Typing
Plug 'jiangmiao/auto-pairs'
Plug 'alvan/vim-closetag'
Plug 'tpope/vim-surround'
" Autocomplete
" https://github.com/SirVer/ultisnips
Plug 'sirver/ultisnips'
Plug 'neoclide/coc.nvim', {'branch':'release'}

" Test
Plug 'tyewang/vimux-jest-test'
Plug 'janko-m/vim-test'

Plug 'edluffy/hologram.nvim'

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
