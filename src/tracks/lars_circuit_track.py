from src.tracks.track import Track
import src.configuration.personal_track_annotations as config


class LarsCircuitTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Lars Circuit"
        self._ui_description = "Lars Circuit is a pro difficulty track that adds an increasing to decreasing double apex and multiple high speed straightaways to its shorter cohort Lars Loop. It is named in honor of 2020 AWS DeepRacer League silver medalist Lars Ludvigson (Duckworth)"
        self._ui_length_in_m = 68.68  # metres
        self._ui_width_in_cm = 107  # centimetres   # TODO
        self._world_name = "thunder_hill_pro"
        self._track_sector_dividers = [20, 40, 60]
        self._annotations = config.lars_circuit_annotations
        self._track_width = 1.066

        self._track_waypoints = [(2.324238896369934, 0.3699307516217232), (2.625182032585144, 0.3746175915002823),
                                 (2.9261234998703003, 0.3794712871313095), (3.2270679473876953, 0.38401539623737335),
                                 (3.5280035734176636, 0.38952575623989105), (3.8287309408187866, 0.39860421419143677),
                                 (4.124210000038147, 0.4536280147731304), (4.40489935874939, 0.5611425191164017),
                                 (4.661593437194824, 0.7174970209598541), (4.88608455657959, 0.9173440933227539),
                                 (5.077223539352417, 1.149719625711441), (5.259321689605712, 1.38934302330017),
                                 (5.431831121444702, 1.6359490156173706), (5.593461513519287, 1.889797568321228),
                                 (5.737814903259277, 2.1538085341453552), (5.858532428741455, 2.429450035095215),
                                 (5.963952541351318, 2.7113420963287354), (6.059667110443115, 2.9966864585876465),
                                 (6.148684501647949, 3.2841964960098267), (6.232323884963989, 3.573317050933838),
                                 (6.311285495758057, 3.8637516498565674), (6.386749982833862, 4.155115842819214),
                                 (6.458662509918213, 4.447376489639282), (6.527236223220825, 4.740437984466553),
                                 (6.5694053173065186, 5.037944555282593), (6.563940525054932, 5.338587999343872),
                                 (6.505260944366455, 5.633213996887207), (6.3731138706207275, 5.902260065078735),
                                 (6.153064012527466, 6.104520559310913), (5.879972457885742, 6.230413913726807),
                                 (5.593099355697632, 6.320772171020508), (5.296260118484497, 6.3684093952178955),
                                 (4.9961395263671875, 6.357616424560547), (4.710381507873535, 6.267083168029785),
                                 (4.473099946975708, 6.084691524505615), (4.310672402381896, 5.832710504531859),
                                 (4.2071733474731445, 5.550222873687744), (4.11384391784668, 5.264082431793213),
                                 (4.024803400039672, 4.97657799720764), (3.939342498779297, 4.687987565994263),
                                 (3.8569390773773193, 4.3985090255737305), (3.7768689393997192, 4.1083749532699585),
                                 (3.7001019716262817, 3.8173654079437256), (3.524623394012451, 3.5733954906463623),
                                 (3.3062825202941895, 3.366990566253662), (3.0459330081939697, 3.217813014984131),
                                 (2.753177523612976, 3.1542528867721558), (2.455304503440857, 3.188552975654602),
                                 (2.1775169372558594, 3.3023070096969604), (1.9332579374313354, 3.47723650932312),
                                 (1.7259114384651184, 3.6948983669281006), (1.5570164918899536, 3.9436135292053223),
                                 (1.3042834997177124, 4.100095510482788), (1.0121999084949493, 4.166914582252502),
                                 (0.7157578468322754, 4.126664519309998), (0.4523705095052719, 3.983823537826538),
                                 (0.22542240843176842, 3.786313056945801), (-0.025880545377731323, 3.6215959787368774),
                                 (-0.3082454577088356, 3.519970655441284), (-0.6073516011238098, 3.5331965684890747),
                                 (-0.865549623966217, 3.4234074354171753), (-1.0015471875667572, 3.1795644760131836),
                                 (-1.1152105927467346, 2.9014655351638794), (-1.3447834849357605, 2.715346574783325),
                                 (-1.6406254768371582, 2.671267509460449), (-1.9383935332298279, 2.711468458175659),
                                 (-2.2254295349121094, 2.800850510597229), (-2.47949755191803, 2.9618465900421143),
                                 (-2.710615038871765, 3.1543054580688477), (-2.9143450260162354, 3.375557541847229),
                                 (-3.0876100063323975, 3.6214081048965454), (-3.2302184104919434, 3.88632595539093),
                                 (-3.421488046646118, 4.116549611091614), (-3.6846868991851807, 4.258808374404907),
                                 (-3.980860471725464, 4.305968403816223), (-4.279927015304565, 4.2780280113220215),
                                 (-4.545570135116577, 4.144580006599426), (-4.781447410583496, 3.9577934741973877),
                                 (-5.002734899520874, 3.7538546323776245), (-5.210633993148804, 3.536331534385681),
                                 (-5.397325038909912, 3.300341010093689), (-5.56742787361145, 3.0520869493484497),
                                 (-5.72538161277771, 2.7959184646606445), (-5.8716139793396, 2.5328779220581055),
                                 (-6.006712913513184, 2.2639445066452026), (-6.129593372344969, 1.9892184734344531),
                                 (-6.240038871765137, 1.7092654705047607), (-6.33646297454834, 1.424180507659912),
                                 (-6.41787314414978, 1.1344610452651978), (-6.481732368469238, 0.8403839468955994),
                                 (-6.52603816986084, 0.5427443385124207), (-6.547938585281372, 0.24263250082731247),
                                 (-6.558498382568359, -0.05815967917442322), (-6.566490411758423, -0.35903145372867584),
                                 (-6.571219444274902, -0.6599732637405396), (-6.573245525360107, -0.9609456062316895),
                                 (-6.573061466217041, -1.2619250416755676), (-6.57001256942749, -1.562889039516449),
                                 (-6.564653635025024, -1.8638205528259277), (-6.556941986083984, -2.164700508117676),
                                 (-6.546350955963135, -2.465480089187622), (-6.450646877288818, -2.7459434270858765),
                                 (-6.2797229290008545, -2.993439555168152), (-6.087092399597168, -3.224634528160095),
                                 (-5.883002042770386, -3.4458165168762207), (-5.672294616699219, -3.6607195138931274),
                                 (-5.4552319049835205, -3.869212508201599), (-5.241199016571045, -4.080813646316528),
                                 (-5.0314881801605225, -4.2967000007629395), (-4.825995445251465, -4.516607999801636),
                                 (-4.624671936035156, -4.740339040756226), (-4.427729368209839, -4.967934846878052),
                                 (-4.235127925872803, -5.199215650558472), (-4.047343969345093, -5.434420585632324),
                                 (-3.8636860847473145, -5.672863483428955), (-3.684948444366455, -5.915018558502197),
                                 (-3.5103789567947388, -6.160160541534424), (-3.2653191089630127, -6.328843116760254),
                                 (-2.9693589210510254, -6.372070074081421), (-2.6734009981155396, -6.321583032608032),
                                 (-2.392390489578247, -6.214606285095215), (-2.1179840564727783, -6.091277122497559),
                                 (-1.8327984809875488, -5.995304107666016), (-1.5420915484428406, -5.917477369308472),
                                 (-1.2481464743614197, -5.852870464324951), (-0.952155351638794, -5.798361539840698),
                                 (-0.6547403931617737, -5.752233505249023), (-0.3561919033527374, -5.714135646820068),
                                 (-0.05575058050453663, -5.707321405410767), (0.24522670358419418, -5.707484483718872),
                                 (0.546178549528122, -5.70350456237793), (0.8470450341701508, -5.6953394412994385),
                                 (1.1477494835853577, -5.682539463043213), (1.4481630325317383, -5.664170980453491),
                                 (1.748169481754303, -5.64012598991394), (2.0474504828453064, -5.608287572860718),
                                 (2.3455244302749634, -5.566688060760498), (2.643517017364502, -5.52452540397644),
                                 (2.9418874979019165, -5.485028028488159), (3.2335950136184692, -5.446614503860474),
                                 (3.457943558692932, -5.250235080718994), (3.547091484069824, -4.963101148605347),
                                 (3.5788004398345947, -4.663931608200073), (3.5895614624023438, -4.363173961639404),
                                 (3.5885199308395386, -4.062206506729126), (3.580720901489258, -3.761334538459778),
                                 (3.566136360168457, -3.46073055267334), (3.501259922981262, -3.1676135063171387),
                                 (3.36588454246521, -2.899688482284546), (3.168731451034546, -2.6733005046844482),
                                 (2.915919542312622, -2.5126320123672485), (2.6209545135498047, -2.467434048652649),
                                 (2.321516990661621, -2.4963214993476868), (2.023238480091095, -2.536244034767151),
                                 (1.7235004901885986, -2.528435468673706), (1.4519020318984985, -2.404777467250824),
                                 (1.2057956159114838, -2.233274459838867), (0.92095747590065, -2.137956976890564),
                                 (0.6238411664962769, -2.09101003408432), (0.32365040481090546, -2.0698944330215454),
                                 (0.022745415568351746, -2.06379097700119), (-0.27822619676589966, -2.0657370686531067),
                                 (-0.5791616141796112, -2.070870578289032), (-0.8800823390483856, -2.076838493347168),
                                 (-1.1809885501861572, -2.0835065245628357), (-1.4818559885025024, -2.091713011264801),
                                 (-1.7826774716377258, -2.1014445424079895), (-2.083446502685547, -2.112699568271637),
                                 (-2.384132981300354, -2.125993013381958), (-2.684725046157837, -2.1406610012054443),
                                 (-2.9857054948806763, -2.140680968761444), (-3.2802380323410034, -2.0959280133247375),
                                 (-3.525309443473816, -1.9265995025634766), (-3.634469985961914, -1.6513915061950684),
                                 (-3.5919026136398315, -1.3560479879379272), (-3.468184471130371, -1.0816726386547089),
                                 (-3.3480050563812256, -0.8057294189929962), (-3.2322698831558228, -0.5278950929641724),
                                 (-3.1234610080718994, -0.24728667736053467),
                                 (-3.0272234678268433, 0.037301450967788696), (-2.780766010284424, 0.20378375053405762),
                                 (-2.48983097076416, 0.27832506597042084), (-2.1899185180664062, 0.29999734461307526),
                                 (-2.1899185180664062, 0.29999734461307526), (-1.8889739513397217, 0.3045971021056175),
                                 (-1.5880314707756042, 0.3093484863638878), (-1.2870870232582092, 0.31397900730371475),
                                 (-0.9861434996128082, 0.3186509907245636), (-0.6851995885372162, 0.32331250607967377),
                                 (-0.3842557966709137, 0.3279755488038063), (-0.08331198245286942, 0.3326387107372284),
                                 (0.21763184666633606, 0.3373008072376251), (0.5185756981372833, 0.3419636934995651),
                                 (0.8195194900035858, 0.34662745147943497), (1.1204630136489868, 0.351289339363575),
                                 (1.4214069843292236, 0.3559514060616493), (1.7223510146141052, 0.36061426252126694),
                                 (2.023294448852539, 0.36528105288743973), (2.324238896369934, 0.3699307516217232)]
