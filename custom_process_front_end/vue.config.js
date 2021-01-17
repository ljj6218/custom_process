module.exports = {
    devServer: {
        proxy: {
            '/api': {
                // target: 'http://127.0.0.1:8209',
                target: 'http://www.golangs.cn',
                changeOrigin: true,
                pathRewrite: {
                    "^/api": "/api"
                }
            }
        }
    }
}
