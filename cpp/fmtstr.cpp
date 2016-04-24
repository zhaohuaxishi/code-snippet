#include <string>
#include <sstream>

inline void BuildFormatString(std::ostringstream& builder,
                              const std::string& fmt_spec,
                              std::string::size_type idx) {
    auto count = fmt_spec.size() - idx;
    if (count <= 0) {
        return;
    }

    builder.write(fmt_spec.data() + idx, count);
}

template <typename T, typename... Types>
void BuildFormatString(std::ostringstream& builder, const std::string& fmt_spec,
                       std::string::size_type idx, const T& first,
                       const Types&... args) {
    auto pos = fmt_spec.find_first_of("{}", idx);
    if (pos == std::string::npos) {
        return BuildFormatString(builder, fmt_spec, idx);
    }

    builder.write(fmt_spec.data() + idx, pos - idx);
    builder << first;
    BuildFormatString(builder, fmt_spec, pos + 2, args...);
}

template <typename... Types>
const std::string FormatString(const std::string& fmt_spec,
                               const Types&... args) {
    std::ostringstream builder;
    BuildFormatString(builder, fmt_spec, 0, args...);
    return builder.str();
}
