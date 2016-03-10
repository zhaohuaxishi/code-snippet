#include <string>
#include <sstream>

using std::stringstream;
using std::string;

void BuildFormatString(std::stringstream& builder,
                       const std::string& fmt_spec) {
    builder << fmt_spec;
}

template <typename T, typename... Types>
void BuildFormatString(std::stringstream& builder,
                       const std::string& fmt_spec,
                       const T& first,
                       const Types&... args) {
    auto pos = fmt_spec.find_first_of("{}");
    if (pos > fmt_spec.length()) {
        builder << fmt_spec;
        return;
    }

    builder << fmt_spec.substr(0, pos);
    builder << first;
    BuildFormatString(builder, fmt_spec.substr(pos + 2), args...);
}

template <typename... Types>
const std::string FormatString(const std::string& fmt_spec,
                               const Types&... args) {
    std::stringstream builder;
    BuildFormatString(builder, fmt_spec, args...);
    return builder.str();
}

