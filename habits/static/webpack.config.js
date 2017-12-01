module.exports = {
  entry: './js/index.js',
  output: {
    path: __dirname + '/dist',
    filename: 'bundle.js'
  },
  module: {
    loaders: [
      {
	loader: 'babel-loader',
	query: {
	  presets: ['react']
	},
	// match files based on pattern
	test: /\.js$/,
	// ignore files matching pattern
	exclude: /node_modules/
      }
    ]
  }
};

