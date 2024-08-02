// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true
// })

// const BundleTracker = require('webpack-bundle-tracker');

// module.exports = {
//     publicPath: "http://0.0.0.0:8080",
//     outputDir: "./dist/",

//     chainWebpack: config => {
//         config.optimization.splitChunks(false)

//         config.plugin('BundleTracker').use(BundleTracker, [
//             {
//                 filename: './webpack-stats.json'
//             }
//         ])

//         config.resolve.alias.set('__STATIC__', 'static')

//         config.devServer
//             .public('http://0.0.0.0:8080')
//             .host('0.0.0.0')
//             .port(8080)
//             .hotOnly(true)
//             .watchOptions({poll: 1000})
//             .https(false)
//             .headers({'Access-Control-Allow-Origin': ['\*']})
//     }
// };



const { defineConfig } = require('@vue/cli-service')
const BundleTracker = require('webpack-bundle-tracker')

module.exports = defineConfig({
  publicPath: process.env.NODE_ENV === 'production' ? '/static/dist/' : 'http://localhost:8080',
  outputDir: '../static/dist',
  indexPath: '../templates/index.html',
  transpileDependencies: true,
  configureWebpack: {
    plugins: [
      new BundleTracker({ path: __dirname, filename: 'webpack-stats.json' }),
    ],
  },
})