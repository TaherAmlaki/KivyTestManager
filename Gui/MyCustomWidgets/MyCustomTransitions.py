from kivy.properties import StringProperty
from kivy.uix.screenmanager import ShaderTransition


class MyFadingTransition:
    fs = """$HEADER
        uniform float t;
        uniform sampler2D tex_in;
        uniform sampler2D tex_out;

        void main(void) {
            vec4 cin = texture2D(tex_in, tex_coord0);
            vec4 cout = texture2D(tex_out, tex_coord0);
            gl_FragColor = mix(cout, cin, t);
        }
    """

    def __init__(self):
        self.transition = ShaderTransition(fs=MyFadingTransition.fs)


class MyWipeTransition(ShaderTransition):
    WIPE_TRANSITION_FS = '''$HEADER$
        uniform float t;
        uniform sampler2D tex_in;
        uniform sampler2D tex_out;

        void main(void) {
            vec4 cin = texture2D(tex_in, tex_coord0);
            vec4 cout = texture2D(tex_out, tex_coord0);
            gl_FragColor = mix(cout, cin, clamp((-1.5 + 1.5*tex_coord0.x + 4.0*t),
                1.0, 2.0));
        }
        '''
    fs = StringProperty(WIPE_TRANSITION_FS)
