# henrietta.rachel.main.py
from _spy.vitollino.main import Cena, Texto, Elemento
from _spy.vitollino.main import INVENTARIO as inv

ILHA = "https://www.fatosdesconhecidos.com.br/wp-content/uploads/2017/08/new-girl-morar-sozinha-1-211.jpg"
TEMPLO = "http://3.bp.blogspot.com/-UsnGAupu3XM/VHvU2M5BHUI/AAAAAAAAdCE/UKbq_5dTM7k/s1600/IMG_6098.JPG"
CORREDOR = "http://i.muyinteresante.com.mx/dam/sociedad/historia/17/03/8/rabbit-hole-700-year-old-secret-knights-templar-cave-network-8-58c006f4a30df__880.jpg.imgo.jpg"
PORTA = "https://www.lojamadersilva.com.br/imagens/produtos/grandes/porta-baia-premium-peroba.jpg"
OCEANO = "https://www.exactsales.com.br/uploads/imagens/800x600_oceano-azul-83-1012.png"
ALGA = "https://i.pinimg.com/originals/70/68/5f/70685fa634c3bb82a8eb5771a0a869ed.png"
CONCHA = "http://www.mat.uc.pt/~picado/conchas/imagens/p10.png"
AQUARIO = "https://www.tenstickers.pt/autocolantes-decorativos/img/preview/autocolante-decorativo-infantil-peixe-aquario-3634.png"
FLORESTA = "https://cdn.pixabay.com/photo/2013/04/26/15/05/denmark-107240_1280.jpg"
CORUJA = "http://www.eternit.com.br/images/files_up/original/29042015150454corujacomasasfechadasnopuleiro_emalta.jpg"
PATOS = "http://4.bp.blogspot.com/-aF5frApwsMs/UnCGJk14WEI/AAAAAAAAahs/FKS72dTtYzk/s1600/Animais-em-png-queroimagem-Cei%C3%A7a-Crispim++(12).png"
MACACO = "https://i.pinimg.com/originals/2e/75/f6/2e75f60ab1931937f8fadcca38630382.png"
FLORES = "https://banner.kisspng.com/20171127/1a3/yellow-rose-bush-png-clipart-picture-5a1bab2ea27e19.9392345015117627346656.jpg"
PASSAROS = "https://png.clipart.me/previews/272/cute-twitter-bird-vector-image-26050.png"
MUSICA = "http://www.daniellebourne.com/wp-content/uploads/2016/03/dd72e5_589684fa9a4348e4993acf52fd5ebd53.jpg_srz_967_857_85_22_0.50_1.20_0.00_jpg_srz.jpeg"
HEADPHONES = "https://images.vexels.com/media/users/3/144117/isolated/preview/b37cdf9a9b5ebc1554ffe1a7825939fc-fones-de-ouvido-de-msica-by-vexels.png"
VIOLAO = "http://cdn5.colorir.com/desenhos/color/201101/024b7852c59f132874fea13c36d4887f_163.png"
CHOCALHO = "https://i.pinimg.com/originals/92/fc/c2/92fcc2e8c29c17242612acef1e457bea.png"
TAMBOR = "https://images.emojiterra.com/emojione/v2/512px/1f941.png"
MUSEU = "https://i.pinimg.com/originals/85/91/e8/8591e8f5722d45c18ea8067e5cbb64e4.jpg"
COROA = "https://medologia.com/assets/images/huol9FtnOB5KjNVjjM04keqhmLYKwIeyd3uEUluBXoPMxBp9J0Wex3CFqBrZt0SL4NPSV9qrNIblOg7pOwjUI6YDqr0SqT4M4Y2n1eU0KWz9saMKCGDYYf8I.png"
VASO = "http://www.fundaj.gov.br/images/stories/museu/museu3.png"
RELOGIO = "http://presidenteprudente.sp.gov.br/museu/images/2028927.png"
LUNETA = "http://www.pngpix.com/wp-content/uploads/2016/07/PNGPIX-COM-Spyglass-Telescope-PNG-Transparent-Image.png"
COZINHA = "https://br.habcdn.com/photos/project/gallery/cozinha-americana-1482703.jpg"
COZINHEIRA = "http://ead.ceiprojac.com.br/Assets/Categorias/M_60371d747e33a01.png"
CADEIRA = "http://www.reformatapecaria.com.br/public/img/default/servicos-de-tapecaria/home/reforma-cadeiras-de-cozinha.png"
PANELA = "https://tramontina.com.br/public/panelas-inox/solar/img/produto.png?v=7"
FOGAO = "http://clipart.coolclips.com/480/vectors/tf05085/CoolClips_hous1104.png"
FOGUEIRA = "https://img.7segundos.com.br/bLgTEmA2KVL3X7YAwuyR2K6dvbM=/460x320/smart/s3.7segundos.com.br/uploads/imagens/74824-fogueiras_jpg.jpeg"
MADEIRA = "http://adrianoesquadrias.com.br/gespress/uploads/2014/12/madeiras.png"
PEDRAS = "https://www.construflama.com.br/wp-content/uploads/2016/02/MG_6242-redux.png"
BARCO = "https://www.urbanarts.com.br/imagens/produtos/047747/Detalhes/pequeno-barco-na-praia.jpg"
REMO = "http://images.tcdn.com.br/img/img_prod/376504/3185_1_20140521111527.png"
PRAIA = "https://png.pngtree.com/element_origin_min_pic/16/07/23/2257937d4f98949.jpg"
COCO = "https://icon-icons.com/icons2/645/PNG/512/bebida_icon-icons.com_59604.png"
SOL = "https://cdn.pixabay.com/photo/2017/07/07/17/29/sun-2482114_960_720.png"
GUARDA_SOL = "https://cdn.pixabay.com/photo/2013/07/13/12/18/bathing-159587_960_720.png"
BALDE = "https://i.pinimg.com/originals/27/0a/fd/270afd56dac1bbf56e985374905c0abf.png"


def criarcenas():
   ilha = Cena(img=ILHA)
   templo = Cena(img=TEMPLO, esquerda=ilha)

criarcenas()
