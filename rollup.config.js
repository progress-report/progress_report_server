import resolve from 'rollup-plugin-node-resolve';
import commonjs from 'rollup-plugin-commonjs'
import babel from 'rollup-plugin-babel';
import sass from 'rollup-plugin-sass';
import replace from 'rollup-plugin-replace';

export default {
  name: 'progressreport',
  input: 'app/src/index.js',
  output: {
    file: 'app/public/js/app.js',
    format: 'iife'
  },
  plugins: [
    sass({
       output: 'app/public/css/style.css',
       insert: false
    }),
    resolve(),
    commonjs({
     include: 'node_modules/**',
     namedExports: {
       'node_modules/react/react.js': ['Children', 'Component', 'createElement'],
       'node_modules/react-dom/index.js': ['render'],
       'node_modules/date-fns/index.js': ['format']
     }
   }),
    babel({
      exclude: 'node_modules/**'
    }),
    replace({
      'process.env.NODE_ENV': '\'' + process.env.NODE_ENV + '\''
    })
  ]
};
