import pytest
import yaml


# 参数化要求传递列表，yaml 默认是一个字典，只会传递所有的 key，配置文件需要使用列表模式，需要在配置文件中加 - 符号，内容加缩紧
@pytest.mark.parametrize('env', yaml.safe_load(open('./env.yml')),ids=['环境'])
def test_yaml(env):
    if 'test' in env:
        print('这是测试环境')
        print('测试环境的IP:%s' % env['test'])
    elif 'dev' in env:
        print('这是开发环境')
        print('开发环境的IP:%s' % env['dev'])
