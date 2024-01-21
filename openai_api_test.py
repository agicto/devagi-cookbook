import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # 读取本地 .env 文件，里面定义了 OPENAI_API_KEY


def openai_module():
    try:

        # Try to import the openai library
        import openai
        from openai import OpenAI
        # If the import is successful, print a confirmation message
        print("OpenAI library is installed. Version is: ", openai.__version__)
        return True

    except ImportError:
        try:
            # Try to import the openai library
            import openai
            # If the import is successful, print a confirmation message
            print(f"OpenAI Version ", openai.__version__, " is too low, please upgrade: pip install -U openai")

        except ImportError:
            # If the openai library is not installed, this block will execute
            print("The OpenAI library is not installed.")
            print("To install the OpenAI library, run: pip install openai")
        finally:
            return False


def test_openai_connection():
    try:
        import openai
        from openai import OpenAI
        client = openai.OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL")
        )
        # 尝试发送一个简单的请求
        response = client.completions.create(model="davinci", prompt="Hello, world!",  max_tokens=5)

        # 如果请求成功，打印响应
        print("连接成功。")
        print(response)
        print(f"响应文本: {response.choices[0].text}")
    except openai.APIConnectionError:
        print(f"API 连接错误：检查网络设置、代理、SSL 或防火墙。当前的Key {openai.api_key} 和URL {openai.base_url}")
    except openai.APITimeoutError:
        print("API 超时错误：稍后重试。请检查代理。{openai.base_url}")
    except openai.AuthenticationError:
        print("认证错误：API 密钥或令牌无效、过期或已撤销。{openai.api_key}")
    except openai.BadRequestError as e:
        print(f"错误的请求：{e}")
    except openai.ConflictError:
        print("冲突错误：资源被另一个请求更新。请重试更新。")
    except openai.InternalServerError:
        print("内部服务器错误：稍后重试。")
    except openai.NotFoundError:
        print("未找到错误：请求的资源不存在。检查资源标识符。")
    except openai.PermissionDeniedError:
        print("权限拒绝错误：检查 API 密钥和资源访问权限。")
    except openai.RateLimitError:
        print("速率限制错误：降低请求频率。参见速率限制指南。")
    except openai.UnprocessableEntityError:
        print("无法处理的实体错误：请重试请求。")
    except Exception as e:
        print(f"其他意外：{e}")

if __name__ == "__main__":
    if openai_module():
        test_openai_connection()
