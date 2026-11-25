const overlay = document.getElementsByClassName('section_overlay');


function buttonexternal(){
    overlay.innerHTML = "<div class="overlay">
                    <ul class="navbar-nav" id="overlay_ul">
                        <li class="nav-item"><!-- List all links  -->
                            <a class="nav-link active" aria-current="page" href="{% url 'pagina001' %}">Inico</a><!-- page home -->
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="{% url 'suppliers' %}">Empresas</a><!-- page enterprises -->
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="{% url 'photos' %}">Fotos</a><!-- page photos -->
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active"  aria-current="page" href="{% url 'infor' %}">Sobre</a><!-- page about -->
                        </li>
                    </ul>
                </div>"
};
