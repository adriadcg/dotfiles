" =================================================
"
"              Mappings config
"
" =================================================

let g:mapleader = ' ' " Define space like leader key
" Save file <leader> + s
nnoremap <leader>w <cmd>w<CR>
" Open init.vim file
nnoremap <leader>e <cmd>e $MYVIMRC<CR> 
" Save and quit
nnoremap <leader>wq <cmd>wq<CR> 
" Use <leader> + y to copy at clipboard
vnoremap <leader>y "+y
nnoremap <leader>y "+y

" Use <leader> + d to cut at clipboard
vnoremap <leader>d "+d
nnoremap <leader>d "+d

" Use <leader> + p to paste from clipboard
vnoremap <leader>p "+p
nnoremap <leader>p "+p
nnoremap <leader>P "+P
vnoremap <leader>P "+P

" Buffer
" Move to next buffer
nnoremap <leader>l <cmd>bnext<CR> 
" Move to previus buffer
nnoremap <leader>h <cmd>bprevious<CR> 
" Close current buffer
nnoremap <leader>q <cmd>bdelete<CR>
" Show all buffers
nnoremap <leader>b <cmd>Telescope buffers<CR> 
" map <leader>f <cmd>find
" Pluggins
" Mover with 2 characters searchs
nmap <leader>m <Plug>(easymotion-s2) 
" Show Tree file view
nmap <leader>ff <cmd>Telescope find_files<CR> 
" Show Color Highlith
nmap <leader>ch <cmd>ColorHighlight<CR>

" Split resize
nnoremap <leader>> 10:<C-w>>
nnoremap <leader>< 10:<C-w><

"
" map <leader>f <cmd>Files<CR>

" Faster scrolling
nnoremap <C-j> 10<C-e>
nnoremap <C-k> 10<C-y>

" Unicode vim
map <leader>u <cmd>UnicodeSearch! 
