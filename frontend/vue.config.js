module.exports = {
  publicPath: '',
  outputDir: '../dist',
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
      },
    },
    historyApiFallback: true,
  },
};
