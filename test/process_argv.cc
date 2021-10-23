#include <node_embedding_api.h>
#include <cstdio>
#include <thread>

static napi_value napi_entry(napi_env env, napi_value exports) {
	napi_value script_string;
	if (napi_ok != napi_create_string_utf8(env,
	        "console.log(process.argv[1], process.argv[2])",
	        NAPI_AUTO_LENGTH,
	        &script_string)) {
		printf("napi_create_string_utf8 failed\n");
		return nullptr;
	}

	napi_value result;
	if (napi_ok != napi_run_script(env, script_string, &result)) {
		printf("napi_run_script failed\n");
		return nullptr;
	}
	return nullptr;
}


int main(int argc, char** argv) {
	const char* process_args[] = { argv[0], "hello", "node" };
	node_run_result_t res = node_run(node_options_t { 3, (const char* const*)process_args, napi_entry });
	if (res.error) {
		printf("%s\n", res.error);
	}
	printf("exit code: %d\n", res.exit_code);
	return 0;
}
