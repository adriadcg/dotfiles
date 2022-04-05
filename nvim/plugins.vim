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
" Highlight UI elements based on current mode
" https://github.com/mvllow/modes.nvim
Plug 'mvllow/modes.nvim'

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
